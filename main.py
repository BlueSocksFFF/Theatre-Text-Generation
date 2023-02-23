# -*- coding: utf-8 -*-
from languageModels.GPT3gen import monologue_generator as gpt3
from api_client import write_to_api, append_to_api, read_from_api
from prompt_engineer import engineer
from analyze_text import key_phrases_from_text

from dotenv import load_dotenv
import os

load_dotenv()

GPT3_API_KEY = os.getenv("GPT3_API_KEY")

## we need a situation for when the suggestion is just a single word, 
# and a seperate situation for chunks of text grabbed from improv scenes

        # scene_text = pull_down_scene_text()
        # suggestion = pull_down_suggestion()

# ^^ normally would be pulling the text/suggestion from the API, hardcoding it for now
# will the scene text be in a LIST form?

scene_text = "well you don't know anything. You never have, you are a fool. Go ahead cousin, try and betray me."
suggestion = "mall"


prompt = engineer(scene_text)
print("engineered prompt:", prompt)

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




