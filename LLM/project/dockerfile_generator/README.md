# Dockerfile Generator

A GenAI powered tool that generates optimized Dockerfiles based on programming language input. This project uses Ollama with the Llama3 model to create Dockerfiles following best practices.


## Prerequisites

 > **Installing Ollama:** ***[Go to Installing Ollama](https://github.com/abcofdevops/aiops/blob/main/LLM/local_hosting_llm/README.md)***

## Setup

 > **Setup project:** ***[Go to Setup Guide](https://github.com/abcofdevops/aiops/edit/main/LLM/project/README.md)***


## Run the Application

**Running Application**
  ```bash
  pip3 install -r requirements.txt
  python3 dockerfile_generator.py
  ```

##  How It Works

1. The script takes a programming language as input (e.g., Python, Node.js, Java)
2. Connects to the Ollama API running locally
3. Generates an optimized Dockerfile with best practices for the specified language
4. Returns the Dockerfile content with explanatory comments


##  Example Usage

```bash
python3 dockerfile_generator.py
Enter programming language: python

# Generated Dockerfile will be displayed...
```
