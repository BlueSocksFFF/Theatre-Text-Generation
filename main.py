import sys
from revChatGPT import monologue_generator as rev_generator

type_of_generator = sys.argv[0]

prompts = []
file1 = open('prompt.txt', 'r')
lines = file1.readlines()
for line in lines:
    prompts.append(line)
file1.close()
match type_of_generator:
    case "rev_generator": generator = rev_generator()
for prompt in prompts:
    generator.generate(prompt)
