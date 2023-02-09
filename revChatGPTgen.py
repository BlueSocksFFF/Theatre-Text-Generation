from revChatGPT.Official import *
import argparse
import sys

from dotenv import load_dotenv
import os

load_dotenv()


CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")


class monologue_generator:
    def __init__(self):
        self.args = {"api": CHATGPT_API_KEY, 
                     "temperature": 0.5,
                     "stream":True}
        self.chatbot = Chatbot(api_key=self.args['api'])

    def generate(self, prompt, audience_suggestion):
        if not self.args['stream']:
            response = self.chatbot.ask(prompt, temperature=self.args['temperature'])
            fo = open("chatgpt_generated_text.txt","a")
            fo.write("ChatGPT from " + audience_suggestion + ": " + response)
            fo.close()
            print("ChatGPT: " + response["choices"][0]["text"])
        else:
            print("ChatGPT: ")
            for response in self.chatbot.ask_stream(prompt, temperature=self.args['temperature']):
                print(response, end="")
                sys.stdout.flush()
            print()