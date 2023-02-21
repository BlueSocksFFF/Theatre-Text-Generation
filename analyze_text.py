import json
import boto3
import nltk

## This file is building out ability to take in text and seperate it into keywords using AWS



def key_phrases_from_text(text): ##using AWS service to pull key words
    comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')

    print(text)

    print('Calling DetectKeyPhrases')

    response = json.loads(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))['KeyPhrases']
    
    phrases = []

    for keyPhrase in response:
        phrases.append(keyPhrase['Text'])

    return phrases


test_phrase = "huh well, the best day I have had was swimming in the Atlantic with my grandma"

phrases = key_phrases_from_text(test_phrase)

print(phrases)



