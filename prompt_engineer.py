from api_client import read_from_api
import json
  


def pull_down_suggestion(): ##pull the single word suggestion from Digital Ocean
    suggestion = read_from_api("avatar_text")
    return suggestion


def suggestion_to_prompt(): ##place suggestion into larger prompt
    suggestion = pull_down_suggestion()
   
    f = open('prompts.json')

    data = json.load(f)

    for i in data['prompts']:
        print(i)
    f.close()


suggestion_to_prompt()
