# Docker Model Runner
This repository help to understand how to run LLM models on your system using Docker. It provides a simple setup if you are already familiar with Docker and want to run a LLM model without running extra application on your system.

## Table of contents

- [Prerequisites](#Prerequisites)
- [Docker Model Runner](#Docker-Model-Runner)
- [Running a Model](#running-a-model)
- [Running a model with UI](#running-a-model-with-ui)

## Prerequisites
- Docker installed on your system.
- Docker Desktop running above version 4.40+.

> If docker desktop is already running above version 4.40+ jump to [Docker Model Runner Usage](##Docker-Model-Runner-Usage)

#### Verify Docker Engine Installed and running
```bash
docker --version
```
#### Install docker model package
```bash
sudo apt-get install docker-model-plugin
```


## Docker Model Runner
You can run the following command to check docker model runner is installed:
```bash
docker model -h
```

If you see the help message for the `docker model` command, it means you are ready to run models using Docker.
It looks like this:
```
Usage:  docker model COMMAND

Commands:
  inspect     Display detailed information on one model
  list        List the available models that can be run with the Docker Model Runner
  pull        Download a model
  rm          Remove a model downloaded from Docker Hub
  run         Run a model with the Docker Model Runner
  status      Check if the Docker Model Runner is running
  version     Show the Docker Model Runner version
```

> Official Documentation
> - Docker Model Runner Docs: [Docker Model Runner](https://docs.docker.com/ai/model-runner/)
> - Docker Hub Models: [ai | Docker Hub](https://hub.docker.com/u/ai)


## Running a Model
#### **Step 1:** Pull the model 
Pull the model you want to run. For example, to pull the `smollm2` model, you can use the following command:
```bash
docker model pull ai/smollm2
```

#### **Step 2:** List the models
After pulling the model, you can check the list of available models by running:
```bash
docker model list
```
#### **Step 3:** Run the model
To run a model, you can use the `docker model run` command followed by the model name. For example, to run the `smollm2` model, you can use the following command:
```bash
docker model run ai/smollm2
```

> If you run 
> ```bash
> docker model run ai/smollm2
> ```
> It will directly pull and run the model 

### Interacting with running model
```bash
docker model run ai/smollm2 “What is DevOps?”
```


## Running a model with UI
Integrate the model/LLM with the application

#### Example Application
Clone the repository
```bash
git clone https://github.com/docker/hello-genai.git
```
#### Move to your application repository
```bash
cd hello-genai/
```

#### Add or change model configuration
```bash
vim .env
```
>```bash
># Configuration for the LLM service
>LLM_BASE_URL=http://model-runner.docker.internal/>engines/llama.cpp/v1	
># Configuration for the model to use
>LLM_MODEL_NAME=ai/smollm2
>```

#### Run the application
```bash
./run.sh
```
#### Access the application
```bash 
http://localhost:8081/
```


