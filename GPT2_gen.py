import requests
from dotenv import load_dotenv
import os

load_dotenv()


GPT2_API_KEY = os.getenv("GPT2_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/gpt2-large"
headers = {"Authorization": GPT2_API_KEY} 

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Write a monologue based off the word artist ",
})

print(output)