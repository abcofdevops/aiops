import ollama
import sys

model_version = "llama3.2:1b"
messages = []  # this will store the chat history

print("Chat started! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model=model_version,
        messages=messages
    )

    reply = response['message']['content']
    print(f"AI: {reply}\n")

    # Add assistant message to history
    messages.append({"role": "assistant", "content": reply})
