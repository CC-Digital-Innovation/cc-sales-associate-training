import logging
import os

import dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, dynamic_prompt
from langchain_chroma import Chroma
from langchain_community.document_loaders import (BSHTMLLoader, CSVLoader,
                                                  Docx2txtLoader, DirectoryLoader,
                                                  PyPDFLoader, TextLoader, UnstructuredPowerPointLoader)
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.checkpoint.memory import InMemorySaver


dotenv.load_dotenv()

REMOTE_HOST = os.getenv('REMOTE_HOST', 'http://localhost:11434')
MODEL_NAME = os.getenv('MODEL_NAME', 'tinyllama')
EMBED_MODEL = os.getenv('EMBED_MODEL', 'nomic-embed-text')
DATA_DIR = os.getenv('DATA_DIR')
CHROMA_DIR = os.getenv('CHROMA_DIR')
SEARCH_K = int(os.getenv('SEARCH_K', 1))
DEBUG_AGENT = os.getenv('DEBUG_AGENT', 'False').lower() in ('true', '1', 't')
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

logger = logging.getLogger(__name__)
if DEBUG:
    # logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)


loader_mapping = {
    '.pdf': PyPDFLoader,
    '.txt': TextLoader,
    '.csv': CSVLoader,
    '.html': BSHTMLLoader,
    '.docx': Docx2txtLoader,
    '.pptx': UnstructuredPowerPointLoader,
}

def custom_loader(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    loader_cls = loader_mapping.get(ext)
    if loader_cls:
        return loader_cls(file_path)

def load_files(directory):
    loader = DirectoryLoader(directory,
                             glob=['**/*.pdf', '**/*.docx', '**/*.csv', '**/*.html', '**/*.txt', '**/*.pptx'],
                             loader_cls=custom_loader,
                             recursive=True)
    return loader.load()

def get_vector_store(embedding, directory=None):
    if directory:
        print('Loading Chroma vector store...')
        return Chroma(
            persist_directory=directory,
            embedding_function=embedding,
        )
    else:
        print('Creating new in-memory vector store...')
        return InMemoryVectorStore(embedding)

def chat(agent):
    print(f"Connected to Ollama at {REMOTE_HOST} using '{MODEL_NAME}'")
    print("Type 'quit', 'exit', or 'bye' to end the chat.\n")

    while True:
        try:
            user_input = input('You: ')
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print('Goodbye!')
                break
            print('\n')

            for step in agent.stream(
                {'messages': [{'role': 'user', 'content': user_input}]},
                {"configurable": {"thread_id": "1"}},
                stream_mode='values',
            ):
                step['messages'][-1].pretty_print()
            print('\n')

        except KeyboardInterrupt:
            print('\nExiting...')
            break
        except Exception as e:
            print(f'\nError: {e}')
            break

def main():
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

    # No data directory or chroma db, skipping RAG
    if DATA_DIR is None and CHROMA_DIR is None:
        agent = create_agent(model, debug=DEBUG_AGENT)
        chat(agent)
        return

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

    # 6. Create middleware for RAG using vector store
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

    # 8. Start chat
    chat(agent)

if __name__ == '__main__':
    main()
