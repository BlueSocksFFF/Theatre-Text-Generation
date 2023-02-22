# -*- coding: utf-8 -*-

from languageModels.GPT3gen import monologue_generator as gpt3
from api_client import write_to_api, append_to_api, read_from_api
from prompt_engineer import pull_down_prompt
from analyze_text import key_phrases_from_text

from dotenv import load_dotenv
import os

load_dotenv()

GPT3_API_KEY = os.getenv("GPT3_API_KEY")

### for setting the prompt for testing by writing to the prompt file ###
# write_to_api("huh well, the best day I have had was swimming in the Atlantic with my grandma", "avatar_prompts")
# ###

# prompt_file = "avatar_prompts" 
# prompt = pull_down_prompt(prompt_file) # grabbing prompt

# print(prompt)

raw_audience_speech = "huh well, the best day I have had was hiking the Himalayas with my friends"
print('raw audience suggestion', raw_audience_speech)

key_phrases = key_phrases_from_text(raw_audience_speech)

parsed_key_phrases = " and ".join(key_phrases)

prompt = f"Write a monologue based on {parsed_key_phrases}. It should be on the spot, a personal story that flits from topic to topic."

print("NEW PROMPT:", prompt)

# instantiate
new_prompt = gpt3(prompt)

monologue = new_prompt.generate() ## Generating a monologue

print("Generated Monologue:", monologue)

write_to_api(monologue, "avatar_text") ## sending that monologue to the API

# ## we may need to adjust write_to_api to be in the longer format with "gesture" and "background"



    




















####  Testing the different language models locally


# match type_of_generator:
#     case "chatgpt": 
#         generator = chatgpt()
#         for prompt in prompts:
#             generator.generate(prompt)
#         set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
#     case "gpt3_generator": 
#         generator = gpt3()
#         for prompt in prompts:
#             generator.generate(prompt)
#         set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
#     case "ai21_generator": 
#         generator = ai21()
#         for prompt in prompts:
#             generator.generate(prompt)
#         set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
#     case "compare": 
#         compare_generators(prompts[0], gpt3(), ai21())
#         set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
#     case other:
#         raise Exception("No generator specified")




