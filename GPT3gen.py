import os
import openai
import json
import sys

from dotenv import load_dotenv

audience_suggestion = sys.argv[2]


load_dotenv()

GPT3_API_KEY = os.getenv("GPT3_API_KEY")


openai.api_key = GPT3_API_KEY 

class monologue_generator:

  def generate(self, Newprompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=Newprompt,
      temperature=0.8,
      max_tokens=300,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )
    fo = open("gpt3_generated_text.txt","a")
    fo.write("\nGPT3 from " + audience_suggestion + ": " + response["choices"][0]["text"])
    fo.close()
    print("GPT3: " + response["choices"][0]["text"])