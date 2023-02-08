import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Write a monologue based off the word artist ",
})

print(output)