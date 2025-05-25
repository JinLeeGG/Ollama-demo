import requests
import json

# Set up the base URL for the local Ollama API
url = "http://localhost:11434/api/chat" # url of the server

payload = {
    "model": "mistral", # model name
    "messages": [{"role": "user", "content": "What is Python?"}] # define different messages 
}

# send the HTTP POST request with streaming enabled
response = requests.post(url, json=payload, stream = True) # sending requets

# Check the response status
if response.status_code == 200:
    print("Streaming response from Ollama")
    for line in response.iter_lines(decode_unicode=True): # go through every line
        if line:    # Ignore empty lines
            try:
                #Parse each line as JSON object
                json_data = json.loads(line)
                # Extract and print the assistant's message content
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                    print(f"\nFailed to parse line: {line}")
    print()     # ensure the final output ends with a newline
else:
    print(f"Error: {response.status_code}")
    print(response.text)


