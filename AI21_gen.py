import requests
import json

##this model seeks to complete a given prompt, doesn't necessarily include the prompt sentence in result

url = "https://api.ai21.com/studio/v1/experimental/j1-grande-instruct/complete"

payload = {
    "numResults": 1,
    "maxTokens": 100,
    "minTokens": 0,
    "temperature": 0.7,
    "topP": 1,
    "topKReturn": 0,
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
    "prompt": "I first experienced art when I was young"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer CmcAHREDKEX167xCGAVqIhVUtcn7PcYU"
}

response = requests.post(url, json=payload, headers=headers)

json_string = (response.text)

json_data = json.loads(json_string)
text = json_data['completions'][0]['data']['text']

print(text)


