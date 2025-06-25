# Crew AI Agent 
CREW_AI_AGENT

Crew AI Agent is a powerful tool designed to assist users in managing and automating tasks within the Crew platform. It leverages advanced AI capabilities to enhance user experience and streamline operations.

## Features
- **Task Automation**: Automate repetitive tasks to save time and reduce errors.
- **Intelligent Assistance**: Get smart suggestions and insights based on user behavior and preferences.
- **User-Friendly Interface**: Easy to navigate and use, even for those with minimal technical knowledge.
- **Integration with Crew Platform**: Seamlessly integrates with the Crew platform to enhance functionality and user experience.
- **Customizable Settings**: Tailor the AI agent to fit specific user needs and preferences.

## Requirements
- Python 3.8 or higher 
- ollama installed and configured  [ollama installation guide](../README.md## Run LLM on local)


## Installation
To install the Crew AI Agent, follow these steps:

- Create a virtual environment
```bash
python3 -m venv crew    
source crew/bin/activate
```
- Install the Crew AI Agent package
```bash
pip3 install crewai
```

## Usage
To create a new Crew AI project, run the following command:
- Add Crew AI project
```bash
crewai create crew crew_ai_project
```
> This will create a new directory named `crew_ai_project` with the necessary files and folders.

> Select a provider when prompted, such as `ollama`, and specify the model you want to use, like `llama3.2:1b`.

> If you want to use different LLM Model or Hosted LLM, you can change the model in the .env file. 

- Navigate to the project directory
```bash
cd crew_ai_project
``` 

>In main.py, change the topic to the one you want to work on, e.g. change `topic: AI LLM's` to `topic: DevOPS` for all the entries of topic.


- Run the Crew AI agent

```bash
crewai install
crewai run
```

- Generated Report

```bash
report.md
```

## Project Structure
```plaintext
crew_ai_project/
├── src/crew_ai_project/
|   ├──config/
│   |   ├── agent.yaml
│   |   └── task.yaml
|   ├── main.py
|   └── crew.py
├── .env
├── report.md
└── uv.lock


```

## Configuration
The configuration files are located in the `config/` directory. The `agent.yaml` file contains the settings for the AI agent, while the `task.yaml` file defines the tasks that the agent can perform.

# Example of `agent.yaml`
```yaml
agent_name 1:
    role:  Role1
    goal:  Goal of the agent

agent_name 2:
    role:  Role2
    goal:  Goal of the agent2
```     
## Example of `task.yaml`
```yaml
Task 1:
    description: Description of Task 1
    command: crew task run task1

Task 2:
    description: Description of Task 2
    command: crew task run task2
```     

## Example of `report.md`
```markdown
# Crew AI Agent Report      
## Overview
This report provides an overview of the Crew AI Agent, its features, and its configuration. 
## Features
- Task Automation
- Intelligent Assistance
- User-Friendly Interface
- Integration with Crew Platform
- Customizable Settings
## Configuration
The configuration files are located in the `config/` directory. The `agent.yaml` file contains the settings for the AI agent, while the `task.yaml` file defines the tasks that the agent can perform.
```


