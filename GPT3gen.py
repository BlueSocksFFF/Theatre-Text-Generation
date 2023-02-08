import os
import openai
import json

openai.api_key = "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"

monologue_generator = openai.Completion.create(
  model="text-davinci-003",
  prompt="Topic: Breakfast\nTwo-Sentence Horror Story: He always stops crying when I pour the milk on his cereal. I just have to remember not to let him see his face on the carton.\n    \nTopic: Water\nTwo-Sentence Horror Story:",
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0
)
print(monologue_generator.choices[0]["text"])