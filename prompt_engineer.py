import json
from analyze_text import key_phrases_from_text


# ------------

def engineer(text):

        if len(text) > 1: #this means TEXT is a longer sentence, not a single suggestion
                print("scene text")
                key_phrases = key_phrases_from_text(text) 
                 ## grabbing the key phrases from scene text in analyze_text.py
                print("key phrases", key_phrases)
                
                ## making the key phrases work syntactically to be put into prompt
                parsed_key_phrases = " and ".join(key_phrases)
                prompt = f"Develop a monologue that examines the role of {parsed_key_phrases} in society and its impact on individuals."
        else:
                print("single suggestion")
                prompt = f"Develop a monologue that examines the role of {text} in society and its impact on individuals."
        return prompt

