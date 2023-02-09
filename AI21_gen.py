import requests
import json
import sys

from dotenv import load_dotenv
import os

audience_suggestion = sys.argv[2]

load_dotenv()


class monologue_generator:
    def __init__(self):
        self.AI21_API_KEY = os.getenv("AI21_API_KEY")
        self.url = "https://api.ai21.com/studio/v1/experimental/j1-grande-instruct/complete"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": self.AI21_API_KEY
        }

    def generate(self, NewPrompt):
        self.complete_prompt(NewPrompt, 1, 100, 0, 0.7, 1, 0)

    def complete_prompt(self, prompt, num_results, max_tokens, min_tokens, temperature, top_p, top_k_return):
        payload = {
            "numResults": num_results,
            "maxTokens": max_tokens,
            "minTokens": min_tokens,
            "temperature": temperature,
            "topP": top_p,
            "topKReturn": top_k_return,
            "frequencyPenalty": {
                "scale": 1,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True
            },
            "presencePenalty": {
                "scale": 0,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True
            },
            "countPenalty": {
                "scale": 0,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True
            },
            "prompt": prompt
        }

        response = requests.post(self.url, json=payload, headers=self.headers)

        json_string = (response.text)

        json_data = json.loads(json_string)

        
        text = json_data['completions'][0]['data']['text']
        
    
        fo = open("ai21_generated_text.txt","a")
        fo.write("\nAI21 from " + audience_suggestion + ": " + text)
        fo.close()
        print("AI21: " + text)

    

