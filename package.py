import ollama 

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "llama2"  # model name
prompt = "What is Python?"

# send the query to the model
response = client.generate(model=model, prompt=prompt)

# print the response from the model
print("Response from Ollama: ")
print(response.response)

