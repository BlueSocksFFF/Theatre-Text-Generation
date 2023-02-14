import sys
from languageModels.revChatGPTgen import monologue_generator as chatgpt
from languageModels.GPT3gen import monologue_generator as gpt3
from languageModels.AI21_gen import monologue_generator as ai21
from helpers import set_one_word_prompt, compare_generators, manage_prompt_wrappers
from api_client import write_to_api, append_to_api, read_from_api, format_for_api

from dotenv import load_dotenv
import os

##this file is for comparing language models, you are able to call which model you would like along with
## the audience prompt, or have them all try the same prompt and examine the results

load_dotenv()

GPT3_API_KEY = os.getenv("GPT3_API_KEY")
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
AI21_API_KEY = os.getenv("AI21_API_KEY")
GPT2_API_KEY = os.getenv("GPT2_API_KEY")


type_of_generator = sys.argv[1] ##will either be a specific language model, an api_call, or a comparison of models
audience_suggestion = sys.argv[2]
print("TYPE:", type_of_generator)
print("NEW PROMPT:", audience_suggestion)

## changing the word PROMPT in prompts.txt to accomodate the improv standard of a one word prompt
set_one_word_prompt("PROMPT_PLACEHOLDER", audience_suggestion)

## Wrapping the audience suggestion in prompt engineering (found in prompts.txt)

prompts = [] 
manage_prompt_wrappers(prompts, 3) ##different prompt_wrapper options located in prompts.py

print("PROMPTS", prompts)

## Sending a generated monologue to the Avatar API-- set to the GPT3 model right now
## Avatar API file name set to "avatar_text" currently
match type_of_generator:
    case "write_api":
        text = gpt3().generate(prompts[0])["choices"][0]["text"]
        background = "https://tinyurl.com/ysf4n5u8"
        gesture = "left"
        ##print("TEXT HERE", text)
        content = format_for_api(text, background, gesture)
        response = write_to_api(content, "avatar_text")
        set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
        if response.status_code == 201:
            print("Text written to {} successfully.".format("avatar_text"))
            exit()
        else:
            print(response)
            print("Failed to write text to API.")
            exit()
    case "append_api":
        text = gpt3().generate(prompts[0])
        response = append_to_api(text, "avatar_text")
        set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
        if response.status_code == 200:
            print("Text appended to {} successfully.".format("avatar_text"))
            exit()
        else:
            print("Failed to append text to API.")
            exit()
    case "read_api":
        response = read_from_api("avatar_text")
        print(response)
        exit()


####  Testing the different language models locally
match type_of_generator:
    case "chatgpt": 
        generator = chatgpt()
        for prompt in prompts:
            generator.generate(prompt)
        set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
    case "gpt3_generator": 
        generator = gpt3()
        for prompt in prompts:
            generator.generate(prompt)
        set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
    case "ai21_generator": 
        generator = ai21()
        for prompt in prompts:
            generator.generate(prompt)
        set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
    case "compare": 
        compare_generators(prompts[0], gpt3(), ai21())
        set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
    case other:
        raise Exception("No generator specified")




