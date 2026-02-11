import io
import logging
import os
import struct

import dotenv
import pyaudio
import pyttsx3
import pvporcupine
import whisper
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, dynamic_prompt
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.checkpoint.memory import InMemorySaver

from rag import get_vector_store, load_files
from speech_to_speech import record_command, transcribe_audio, speak


dotenv.load_dotenv()

REMOTE_HOST = os.getenv('REMOTE_HOST', 'http://localhost:11434')
MODEL_NAME = os.getenv('MODEL_NAME', 'tinyllama')
EMBED_MODEL = os.getenv('EMBED_MODEL', 'nomic-embed-text')
DATA_DIR = os.getenv('DATA_DIR')
CHROMA_DIR = os.getenv('CHROMA_DIR')
SEARCH_K = int(os.getenv('SEARCH_K', 1))
DEBUG_AGENT = os.getenv('DEBUG_AGENT', 'False').lower() in ('true', '1', 't')
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

PORCUPINE_ACCESS_KEY = os.environ["PORCUPINE_ACCESS_KEY"]
KEYWORD_PATH = os.environ['KEYWORD_PATH']

logger = logging.getLogger(__name__)
if DEBUG:
    # logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)

# Load Whisper
whisper_model = whisper.load_model("base")

# load TTS engine
tts_engine = pyttsx3.init()

# Setup constants
CHUNK_DURATION = 0.5  # seconds per chunk
SILENCE_THRESHOLD = 200
SILENCE_DURATION = 2.0

def send_to_model(text, agent):
    result = agent.invoke(
                {'messages': [{'role': 'user', 'content': text}]},
                {"configurable": {"thread_id": "1"}},
                stream_mode='values')
    logger.debug(f'Model response: {result["messages"][-1].content}')
    speak(result['messages'][-1].content)

def main():
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_ACCESS_KEY,
        keyword_paths=[KEYWORD_PATH],
        sensitivities=[0.7]
    )

    # Validate K is not larger than 4. If RAG context is too large, 
    # API query will indefinitely loop.
    if SEARCH_K > 4:
        raise ValueError('SEARCH_K cannot be larger than 4 to prevent infinite loop.')

    # 1. Setup models
    model = ChatOllama(
        model=MODEL_NAME,
        temperature=0,
        base_url=REMOTE_HOST
    )
    embedding = OllamaEmbeddings(model=EMBED_MODEL, base_url=REMOTE_HOST)

    # 2. Load or create vector store
    vector_store = get_vector_store(embedding, CHROMA_DIR)
    print('Vector store is ready.')

    if DATA_DIR is not None:
        # 3. Load documents
        print('Loading documents...')
        docs = load_files(DATA_DIR)
        print(f'Found {len(docs)} documents.')
        logger.debug('\n\n'.join(f'{i+1}. Loaded Document {doc.metadata}' for i, doc in enumerate(docs)))
        # 4. Split documents into chunks
        print('Splitting documents into chunks...')
        splits = RecursiveCharacterTextSplitter().split_documents(docs)
        print(f'Created {len(splits)} document chunks.')

        # 5. Add documents to vector store
        print('Adding chunks to vector store...')
        vector_store.add_documents(splits)
        print('Chunks added to vector store.')

    @dynamic_prompt
    def prompt_with_context(request: ModelRequest) -> str:
        last_query = request.state['messages'][-1].text
        retrieved_docs = vector_store.similarity_search(last_query, k=SEARCH_K)

        logger.debug('\n'.join(f'RAG Document {doc.metadata}:\n{doc.page_content[:200]}\n' for doc in retrieved_docs))

        docs_content = '\n\n'.join(doc.page_content for doc in retrieved_docs)

        system_message = (
            'You are a helpful assistant. Use the following context in your response:'
            f'\n\n{docs_content}'
        )

        return system_message

    # 7. Create agent with RAG middleware
    agent = create_agent(model, tools=[], middleware=[prompt_with_context], checkpointer=InMemorySaver(), debug=DEBUG_AGENT)

    pa = pyaudio.PyAudio()

    try:
        while True:
            print("👂 Listening for wake word...")
            stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length
            )

            try:
                while True:
                    pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
                    pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)

                    if porcupine.process(pcm_unpacked) >= 0:
                        print("✅ Wake word detected!")
                        break  # Exit inner loop to start recording

            finally:
                stream.stop_stream()
                stream.close()

            raw_audio = record_command(
                pa,
                porcupine.sample_rate,
                int(porcupine.sample_rate * CHUNK_DURATION)
            )

            raw_audio.seek(0, io.SEEK_END)
            size_in_bytes = raw_audio.tell()
            raw_audio.seek(0)

            num_samples = size_in_bytes // 2
            if num_samples < porcupine.sample_rate * 2:
                print("⏱️ No speech detected.")
                continue

            try:
                transcript = transcribe_audio(raw_audio, porcupine.sample_rate)
                if transcript:
                    print(f"🗣️ You said: {transcript}")
                    send_to_model(transcript, agent)
                else:
                    print("🤐 No transcribable speech detected.")
            except Exception as e:
                print(f"❌ Error during transcription: {e}")

    except KeyboardInterrupt:
        print("👋 Exiting...")

    finally:
        pa.terminate()
        porcupine.delete()

if __name__ == "__main__":
    main()
