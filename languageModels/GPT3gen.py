import os
import openai
from dotenv import load_dotenv

load_dotenv()

GPT3_API_KEY = os.getenv("GPT3_API_KEY")


openai.api_key = GPT3_API_KEY 

class monologue_generator:

  def __init__(self, prompt) -> None:
    self.prompt = prompt

  def generate(self):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=self.prompt,
      temperature=0.8,
      max_tokens=300,
      # top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )["choices"][0]["text"]
    # fo = open("generatedTexts/gpt3_generated_text.txt","a")
    # fo.write("\nGPT3 from " + self.prompt + ": " + response)
    # fo.close()
    with open("generatedTexts/gpt3_generated_text.txt", "a", encoding="utf-8") as fo:
        fo.write("\nGPT3 from " + self.prompt + ": " + response.encode('utf-8').decode('utf-8'))
    return response

    