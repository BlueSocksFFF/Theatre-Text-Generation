from api_client import read_from_api
import json
  


# not doing pull down SUGGESTION yet, working as if there is already engineered prompt

    # def pull_down_suggestion(): ##pull the single word suggestion from the API
    #     suggestion = read_from_api("avatar_text")
    #     return suggestion, word


def pull_down_prompt(file_name): ##pull the single word suggestion from the API
        prompt = read_from_api("avatar_text")["content"]
        return prompt


# Not converting suggestion to prompt, assuming already engineered prompt

    # def suggestion_to_prompt(): ##place suggestion into larger prompt
    #     suggestion, word = pull_down_suggestion()
    
    #     f = open('prompts.json')
    #     data = json.load(f)
    #     prompt = data["content"]

    #     f.close()


