from api_client import read_from_api
import json



def pull_down_prompt(file_name): ##pulling a fully engineered prompt
        prompt = read_from_api("avatar_text")["content"]
        return prompt




def pull_down_suggestion(): ##pulling the single word suggestion from the API
        suggestion = read_from_api("suggestions")
        return suggestion



