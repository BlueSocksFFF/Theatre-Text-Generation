import json
from languageModels.GPT3gen import monologue_generator as gpt3


location = "new york city"
occupation = "doctor"
problem = "work life balance"

emotion1 = "pessimistic"
emotion2= "optimistic"


prompt = "Create a monologue that takes place in {} about someone who works as a {} dealing with {}. The monologue should begin {} and end {}.".format(location, occupation, problem, emotion1, emotion2)

prompt2 = "Create a monologue that discusses {} in broad terms. Connect it to a personal story, and write it as though it is made up on the spot. The monologue should begin {} and end {}.".format(problem, emotion1, emotion2)

prompt3 = "Create a monologue that discusses {}. This monologue should sound like it was made up on the spot. Use personal anecdotes, filler words like 'ah' 'um' or 'like', rhetorical questions, and varied sentence length. I want a natural tone and feeling. The monologue should begin {} and end {}.".format(problem, emotion1, emotion2)

prompt4 = "Create a monologue that discusses {}. This monologue should sound like it was made up on the spot. Use two separate personal anecdotes, filler words like 'ah' 'um' or 'like', rhetorical questions, and varied sentence length. I want a natural tone and feeling. The monologue should begin {} and end {}.".format(problem, emotion1, emotion2)

print("prompt: ", prompt4)


# instantiate gpt3 model
gpt = gpt3()
# generate monologue
monologue = gpt.generate_monologue(prompt=prompt4)
print("Generated Monologue:", monologue)

