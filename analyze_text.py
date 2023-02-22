import json
import boto3
import os

## This file is building out ability to take in text and seperate it into keywords using AWS

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

def key_phrases_from_text(text): ##using AWS service to pull key words
    comprehend = session.client(service_name='comprehend', region_name='us-west-2')

    print(text)

    print('Calling DetectKeyPhrases')

    response = json.loads(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))['KeyPhrases']
    
    phrases = []

    for keyPhrase in response:
        phrases.append(keyPhrase['Text'])

    return phrases




