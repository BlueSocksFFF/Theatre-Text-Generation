from languageModels.GPT3gen import monologue_generator as gpt3
from api_client import write_to_api, append_to_api, read_from_api
from prompt_engineer import pull_down_prompt
from analyze_text import key_phrases_from_text

from dotenv import load_dotenv
import os

load_dotenv()

GPT3_API_KEY = os.getenv("GPT3_API_KEY")
type_of_generator = gpt3 


### for setting the prompt for testing by writing to the prompt file ###
write_to_api("huh well, the best day I have had was swimming in the Atlantic with my grandma", "avatar_prompts")
###

prompt_file = "avatar_prompts" 
prompt = pull_down_prompt(prompt_file) # grabbing prompt

print(prompt)

print("TYPE:", type_of_generator)
print("NEW PROMPT:", prompt)


monologue = gpt3().generate(prompt) ## Generating a monologue

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




