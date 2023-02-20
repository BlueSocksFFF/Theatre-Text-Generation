import requests


## this file is for interacting with the Avatar API

def write_to_api(content, file_name):
    url = "http://api.the-singularity-show.com/api/write/"
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "content": content, ##content needs to be in segmented json format eventually
        "file": file_name
    }
    response = requests.post(url, headers=header, json=data)
    return response

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


def read_latest_from_api(file_name):
    url = "http://api.the-singularity-show.com/api/latest/"
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "file": file_name
    }
    response = requests.post(url, headers=header, json=data)
    return response.json()


    
#   was attempting to put the json response in a specific format 

# def format_for_api(text, background, gesture): 
#    content = [
#         {
#             "text": text,
#             "gesture": gesture,
#             "background": background,
#             "voice": "",
#             "control": ""
#         }]
#    print(content)
#    return content
