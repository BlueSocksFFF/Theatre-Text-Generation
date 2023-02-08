import os
import openai
import json

openai.api_key = "gpt3key" ##willa has this just deleting from our repo for now lol

class monologue_generator:

  def generate(self, Newprompt, audience_suggestion):
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
    fo.write("GPT3 from " + audience_suggestion + ": " + response["choices"][0]["text"])
    fo.close()
    print("GPT3: " + response["choices"][0]["text"])