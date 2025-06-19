# Run LLM on local

## Installing Ollama

### 1. **Download Ollama**

   - ***Using Web based OLLAMA Application***  [Ollama download](https://ollama.com/download)
   

   - ***Using CLI***
   
     ```bash
     # For Linux
     curl -fsSL https://ollama.com/install.sh | sh

     # For MacOS
     brew install ollama
     ```

### 2. **Ollama user guide**

   ```bash
  Ollama

  Usage:
    ollama [flags]
    ollama [command]

  Available Commands:
    serve		   Start ollama
    create     Create a model from a Modelfile
    show       Show information for a model
    run        Run a model
    stop       Stop a running model
    pull       Pull a model from a registry
    push       Push a model to a registry
    list       List models
    ps         List running models
    cp         Copy a model
    rm         Remove a model
    help       Help about any command

  Flags:
    -h, --help      help for ollama
    -v, --version   Show version information
   ```

### 3. **Start Ollama Service**
   ```bash
   ollama serve
   ```

### 4. **Pull Llama3 Model**
   ```bash
   ollama pull llama3.2:1b
   ```

### 5. **Run Llama3 Model**
   ```bash
   ollama run llama3.2:1b
   ```
