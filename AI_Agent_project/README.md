# AI Agent to read Documents and answer questions.
This project is based on the CrewAI examples repository, specifically the `meta_quest_knowledge` project. It provides a framework for creating AI agents that can read documents and answer questions based on their content.

## Steps to run the project

> Steps to run the project are similar to the [AI_Agent project](../AI_Agent/README.md) with some minor differences.

1. **Clone the repository**: Clone the CrewAI examples repository to your local machine.
``` git
git clone https://github.com/crewAIInc/crewAI-examples

cd crewAI-examples/meta_quest_knowledge
```

2. **Add your documents**: Place your documents in the `knowledge` directory. The agent will read these documents to answer questions.

3. **Agent configuration**: Make changes in config > `agents.yaml` to configure the agent. You can specify the model name and details as per the requirements.

4. **Allow user to ask questions**: Make changes in `main.py` to allow the user to ask questions. The agent will use the documents in the `knowledge` directory to answer these questions.

- Changes
```python
# main.py
def run():
    ...
    question = input("Please enter your question: ")    
    inputs = {
        'question': question,
    }
    ...

def train():
def test():

    'question': 'What is ABC of DevOps?',
```

5. **Pass the PDF to the agent**: In the `crew.py` file, PDF source is set to correct path in `knowledge` directory and the correct agent configuration is used.

```python
# crew.py
pdf_source = PDFKnowledgeSource(
    file_paths=["ABC_of_DevOps_Training_Manual.pdf.pdf"] # Replace with your document name
) 

	@agent
    ...
			config=self.agents_config['abc_of_devops_expert'],
    ...
``` 

6. **Verify Project Name**: Verify the project name in the `pyproject.toml` file. It should match the name of your project.

7. **Install dependencies**:

```bash
pip install uv
```

8. **Install and run CrewAI**: Install CrewAI using the following command:
```bash
crewai install

crewai run
```


> You might need to downgrade to supported version of Python 3.11.9 if you haven't already, as it is required for this project.
```bash 
brew install pyenv
pyenv install 3.11.9
pyenv local 3.11.9
```


> You might need to check and install rust if you haven't already, as it is required for some dependencies.
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
rustc --version
```

> At any point, if you need to change the environment, you can run:
```bash
uv sync
```


