import ollama

model_version = “llama3.2:1b”

PROMPT = """
ONLY Generate an ideal Dockerfile for {language} with best practices. Do not provide any description
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def dockerfile_generator(language):
    response = ollama.chat(model = model_version, messages=[{'role': 'user', 'content': PROMPT.format(language=language)}])
    return response['message']['content']

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = dockerfile_generator(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
