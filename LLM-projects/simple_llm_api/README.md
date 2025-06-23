# Simple LLM API

## Prerequisites

 > **Installing Ollama:** ***[Go to Installing Ollama](https://github.com/abcofdevops/aiops/blob/main/LLM/local_hosting_llm/README.md)***

## Setup

 > **Setup project:** ***[Go to Setup Guide](https://github.com/abcofdevops/aiops/edit/main/LLM/project/README.md)***



## Run the Application

**Running Application**
  ```bash
  python3 app.py Hi
  ```

  ``` bash
  # Output
  Hello. Is there something I can help you with or would you like to chat?
   ```

##  How It Works

1. The script takes a user argument (e.g., Hi)
2. Connects to the Ollama API running locally
3. Generates an Answer
4. Returns the Answer as output

##  Example DevOps Usage

```bash
python3 app.py "Generate a dockerfile without comments"

# Generated Dockerfile will be displayed...
```


