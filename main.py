import sys
from revChatGPTgen import monologue_generator as rev_generator
from GPT3gen import monologue_generator as gpt3_generator
from helpers import set_one_word_prompt

type_of_generator = sys.argv[1]
audience_suggestion = sys.argv[2]
print("TYPE:", type_of_generator)
print("NEW PROMPT:", audience_suggestion)

## changing the word PROMPT in prompts.txt to accomodate the improv standard of a one word prompt
set_one_word_prompt("PROMPT_PLACEHOLDER", audience_suggestion)


prompts = []
file1 = open('prompts.txt', 'r')
lines = file1.readlines()
for line in lines:
    prompts.append(line)
file1.close()
match type_of_generator:
    case "chatgpt_generator": generator = rev_generator()
    case "gpt3_generator": generator = gpt3_generator()
    case other:
        raise Exception("No generator specified")
for prompt in prompts:
    generator.generate(prompt, audience_suggestion)

set_one_word_prompt(audience_suggestion, "PROMPT_PLACEHOLDER")
