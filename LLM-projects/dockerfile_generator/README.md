# Dockerfile Generator

A GenAI powered tool that generates optimized Dockerfiles based on programming language input. This project uses Ollama with the Llama3 model to create Dockerfiles following best practices.


## Prerequisites

 > **Installing Ollama:** ***[Go to Installing Ollama](../../README.md#run-llm-on-local)***

## Setup

 > **Setup project:** ***[Go to Setup Guide](../README.md)***


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
