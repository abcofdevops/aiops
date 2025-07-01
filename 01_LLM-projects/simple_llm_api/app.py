import ollama
import sys

model_version = "llama3.2:1b"

response = ollama.chat(
	model= model_version, 
	messages=[
		{'role': 'user', 'content': sys.argv[1]}
		]
	)

#Output
print(response['message']['content'])
