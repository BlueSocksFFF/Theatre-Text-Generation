import requests
from languageModels.GPT3gen import monologue_generator

## this file is for interacting with the Avatar API

def write_to_api(content, file_name):
    url = "http://api.the-singularity-show.com/api/write/"
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "content": content, ##content needs to be in segmented json format
        "file": file_name
    }
    response = requests.post(url, headers=header, json=data)
    return response

def format_for_api(text, background, gesture): 
   content = [
        {
            "text": text,
            "gesture": gesture,
            "background": background,
            "voice": "",
            "control": ""
        }]
   print(content)
   return content


def append_to_api(content, file_name):
    url = "http://api.the-singularity-show.com/api/append/"
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "content": content,
        "file": file_name
    }
    response = requests.post(url, headers=header, json=data)
    return response


def read_from_api(file_name):
    url = "http://api.the-singularity-show.com/api/read/"
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "file": file_name
    }
    response = requests.post(url, headers=header, json=data)
    return response.json()