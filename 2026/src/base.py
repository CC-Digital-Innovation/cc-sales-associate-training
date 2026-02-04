import os

import dotenv
import ollama


dotenv.load_dotenv()

# --- CONFIGURATION ---
REMOTE_HOST = os.getenv('REMOTE_HOST', 'http://localhost:11434')
MODEL_NAME = os.getenv('MODEL_NAME', 'tinyllama')


def chat_with_ollama():
    # Initialize the client pointing to your remote server
    client = ollama.Client(REMOTE_HOST)
    
    # Store conversation history
    messages = []

    print(f"Connected to Ollama at {REMOTE_HOST} using '{MODEL_NAME}'")
    print("Type 'quit', 'exit', or 'bye' to end the chat.\n")

    while True:
        try:
            user_input = input('You: ')
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print('Goodbye!')
                break

            # Add user message to history
            messages.append({'role': 'user', 'content': user_input})

            print('AI: ', end='', flush=True)

            # Stream the response
            stream = client.chat(
                model=MODEL_NAME, 
                messages=messages, 
                stream=True
            )

            full_response = ''
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end='', flush=True)
                full_response += content

            print('\n')  # Newline after response

            # Add assistant response to history to maintain context
            messages.append({'role': 'assistant', 'content': full_response})

        except KeyboardInterrupt:
            print('\nExiting...')
            break
        except Exception as e:
            print(f'\nError: {e}')
            break

if __name__ == '__main__':
    chat_with_ollama()