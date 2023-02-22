from api_client import read_from_api
import json



def pull_down_prompt(file_name): ##pulling a fully engineered prompt
        prompt = read_from_api("avatar_text")["content"]
        return prompt




def pull_down_suggestion(): ##pulling the single word suggestion from the API
        suggestion = read_from_api("suggestions")
        return suggestion

def key_phrases_to_prompt(keywords): ## taking in keywords (as a list) and making a prompt
    for x in keywords:


   

# Not converting suggestion to prompt, assuming already engineered prompt

    # def suggestion_to_prompt(): ##place suggestion into larger prompt
    #     suggestion, word = pull_down_suggestion()
    
    #     f = open('prompts.json')
    #     data = json.load(f)
    #     prompt = data["content"]

    #     f.close()


