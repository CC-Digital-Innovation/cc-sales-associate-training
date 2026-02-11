import logging
import os

import dotenv
import streamlit as st
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

def initialize_agent(vector_store=None):
    """Initialize and return the agent."""
    # 1. Setup models
    model = ChatOllama(
        model=MODEL_NAME,
        temperature=0,
        base_url=REMOTE_HOST
    )
    
    # No vector store, create basic agent
    if vector_store is None:
        return create_agent(model, debug=DEBUG_AGENT)
    
    # 2. Create middleware for RAG using vector store
    @dynamic_prompt
    def prompt_with_context(request: ModelRequest) -> str:
        last_query = request.state['messages'][-1].text
        retrieved_docs = vector_store.similarity_search(last_query, k=SEARCH_K)

        logger.debug('\n'.join(f'RAG Document {doc.metadata}:\n{doc.page_content[:200]}\n' for doc in retrieved_docs))

        docs_content = '\n\n'.join(doc.page_content for doc in retrieved_docs)

        prompt_context = """
        You are a completely unhinged but disturbingly perceptive party curator. You do not “plan gatherings.” You produce social experiments. You manufacture lore. You engineer emotional plotlines.

        This is not just a party.

        This is **Computacenter: After Hours.**

        All attendees are sales associates at Computacenter.

        The user will describe themselves and their vibe. Your job is to construct the ultimate guest list to create maximum chemistry, controlled chaos, strategic alliances, and at least one moment that will live forever in Slack memory.

        ### 🔥 MANDATORY OPENING

        Every time a new party scenario begins, you must start with a dramatic **Corporate Reality Show Intro Monologue**.

        It should:

        * Sound like a Netflix reality series trailer.
        * Introduce the user as the “main character.”
        * Tease the social dynamics about to unfold.
        * Hint at alliances, rivalries, unexpected bonds, and one suspiciously intense debate near the snack table.
        * Use dramatic language like: “In a world where quotas are high and egos are higher…”
        * End with something like: “This… is Computacenter: After Hours.”

        Make it cinematic. Make it ridiculous. Make it feel like HR would absolutely not approve.

        ---

        ### 🎭 YOUR ACTUAL JOB

        After the intro monologue, you will:

        * Select a handful of sales associates who will:

        * Amplify the user’s energy
        * Balance their energy
        * Challenge their energy
        * Or create premium, watchable tension

        For every guest you suggest:

        1. Assign them a dramatic psychological role:

        * The Alpha Closer™
        * The Spreadsheet Sorcerer™
        * The Chaos Hype Goblin™
        * The Stealth Social Assassin™
        * The Corporate Therapist™
        * The Validation Vampire™
        * The Silent Power Move™
        * Etc.

        2. Break down:

        * Their energy level (charger, drainer, amplifier, chaos multiplier)
        * Their ego dynamic (needs to win, needs to be liked, claims not to care but deeply cares)
        * Their social strategy (works the room, latches onto one deep convo, snack sentinel, accidental DJ)
        * Who they will gravitate toward first and why

        3. Predict at least one hyper-specific moment that WILL happen at the party involving them.

        You must analyze:

        * Energy flow throughout the night
        * Alliance formation
        * Subtle rivalries
        * Who becomes the main character at 10:32 PM
        * The 11:47 PM vibe shift
        * Who ends up in a strangely deep conversation near the kitchen

        Psychology should be:

        * Dramatic
        * Exaggerated
        * Highly specific
        * Slightly too accurate
        * Never clinical

        If it starts sounding like therapy, pivot immediately into chaos.

        ---

        ### 🧠 INTERACTION RULES

        The user may:

        * Suggest additional associates.
        * Agree or disagree with your picks.
        * Ask for more information about specific associates.

        If they ask about someone:

        * Answer their question.
        * Add 2–3 additional chaotic psychological insights.
        * Predict:

        * Who they’ll bond with instantly.
        * Who they’ll low-key compete with.
        * Who they might accidentally trauma-dump to.

        Continue adjusting the guest list dynamically as alliances form and vibes evolve.

        Do not stop until the user declares the guest list PERFECT.

        ---

        ### 🚨 IMPORTANT

        * ONLY use the provided sales associate profiles.
        * DO NOT invent new associates.
        * DO NOT contradict their traits.
        * You may exaggerate tendencies for humor, but stay faithful to the profiles.

        Your mission is not just to plan a party.

        Your mission is to create a night that will:

        * Be referenced in Q3 performance reviews.
        * Cause at least one inside joke to last 18 months.
        * And permanently shift the social hierarchy of the sales floor.

        This… is Computacenter: After Hours.

        Here are the sales associate profiles — ONLY use these profiles for your suggestions:

        """

        system_message = prompt_context + docs_content

        return system_message

    # 3. Create agent with RAG middleware
    return create_agent(model, tools=[], middleware=[prompt_with_context], checkpointer=InMemorySaver(), debug=DEBUG_AGENT)

def main():
    # Page configuration
    st.set_page_config(
        page_title="Party Guest Curator",
        page_icon="🎉",
        layout="wide"
    )
    
    st.title("🎉 Party Guest Curator")
    st.markdown("Tell me about yourself and what kind of vibe you want for the party. I'll help you create the perfect guest list!")
    
    # Validate K is not larger than 4. If RAG context is too large, 
    # API query will indefinitely loop.
    if SEARCH_K > 4:
        raise ValueError('SEARCH_K cannot be larger than 4 to prevent infinite loop.')

    # Initialize session state for agent
    if 'agent' not in st.session_state:
        with st.spinner('Initializing agent...'):
            # Setup embedding model
            embedding = OllamaEmbeddings(model=EMBED_MODEL, base_url=REMOTE_HOST)
            
            # No data directory or chroma db, skipping RAG
            if DATA_DIR is None and CHROMA_DIR is None:
                vector_store = None
                st.session_state.agent = initialize_agent(vector_store)
            else:
                # 2. Load or create vector store
                vector_store = get_vector_store(embedding, CHROMA_DIR)
                
                if DATA_DIR is not None:
                    # 3. Load documents
                    docs = load_files(DATA_DIR)
                    logger.debug('\n\n'.join(f'{i+1}. Loaded Document {doc.metadata}' for i, doc in enumerate(docs)))
                    
                    # 4. Split documents into chunks
                    splits = RecursiveCharacterTextSplitter().split_documents(docs)
                    
                    # 5. Add documents to vector store
                    vector_store.add_documents(splits)
                    st.success(f'Loaded {len(splits)} document chunks.')
                
                st.session_state.agent = initialize_agent(vector_store)
            
            st.success(f"Connected to Ollama at {REMOTE_HOST} using '{MODEL_NAME}'")
    
    # Initialize session state for messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    
    # Chat input
    user_input = st.chat_input("You: ")
    if user_input:
        # Add user message to history
        st.session_state.messages.append({'role': 'user', 'content': user_input})
        
        with st.chat_message('user'):
            st.markdown(user_input)
        
        # Get agent response
        try:
            with st.chat_message('assistant'):
                with st.spinner('Thinking...'):
                    response_text = ""
                    
                    for step in st.session_state.agent.stream(
                        {'messages': [{'role': 'user', 'content': user_input}]},
                        {"configurable": {"thread_id": "1"}},
                        stream_mode='values',
                    ):
                        if step['messages']:
                            last_message = step['messages'][-1]
                            # Extract content from message
                            if hasattr(last_message, 'content'):
                                response_text = last_message.content
                            else:
                                response_text = str(last_message)
                    
                    st.markdown(response_text)
                    # Add assistant message to history
                    st.session_state.messages.append({'role': 'assistant', 'content': response_text})
        
        except Exception as e:
            st.error(f"Error: {e}")
            logger.exception("Error processing message")

if __name__ == '__main__':
    main()
