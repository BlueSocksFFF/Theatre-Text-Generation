import os
import openai
from dotenv import load_dotenv

load_dotenv()

GPT3_API_KEY = os.getenv("GPT3_API_KEY")

openai.api_key = GPT3_API_KEY 

class gpt3_5_monologue_generator:

  def __init__(self) -> None:
     pass

  def generate_monologue(self, prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": prompt}],
      temperature=0.8,
      max_tokens=300,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )["choices"][0]["message"]["content"]
    # fo = open("generatedTexts/gpt3_generated_text.txt","a")
    # fo.write("\nGPT3 from " + self.prompt + ": " + response)
    # fo.close()
    # with open("generatedTexts/gpt3_generated_text.txt", "a", encoding="utf-8") as fo:
    #     fo.write("\nGPT3 from " + prompt + ": " + response.encode('utf-8').decode('utf-8'))
    return response

    