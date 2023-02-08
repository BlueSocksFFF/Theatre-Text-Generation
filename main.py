from revChatGPT.Official import *
import argparse
import sys


class monologue_generator:
    def __init__(self):
        self.args = {"api": "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",
                     "temperature": 0.5,
                     "stream":True}
        self.chatbot = Chatbot(api_key=self.args['api'])

    def generate(self, prompt):
        if not self.args['stream']:
            response = self.chatbot.ask(prompt, temperature=self.args['temperature'])
            print("ChatGPT: " + response["choices"][0]["text"])
        else:
            print("ChatGPT: ")
            for response in self.chatbot.ask_stream(prompt, temperature=self.args['temperature']):
                print(response, end="")
                sys.stdout.flush()
            print()


prompt1 = "Write an armando style monologue based on the word lose weight. Make the story first-person and personal, with themes that are easy to expand on."
prompt2 = "continue"
generator = monologue_generator()
generator.generate(prompt1)
# generator.generate(prompt2)

