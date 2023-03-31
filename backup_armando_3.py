from languageModels.GPT3gen import gpt3_monologue_generator as gpt3
import languageModels.introduction_gen
import json
import random
from helpers import emotion_setter


##setting up the show with an introduction of the improvisers

languageModels.introduction_gen.basic_intro()

# these suggestion specifications should be given to us from the host/audience
suggestion = "oil spills"

# setting new emotions for the monologue
emotion_set_module = emotion_setter()
first_emotion, second_emotion = emotion_set_module.get_emotions()

print(first_emotion, second_emotion)

base_prompt = "Write a monologue that discusses {}. This monologue should sound like it was made up on the spot. Use multiple personal anecdotes, filler words like 'ah' 'um' or 'like', rhetorical questions, and varied sentence length. Do not begin with a filler word. I want a natural tone and feeling. The monologue should begin with the emotion {} and end with the emotion {}.".format(suggestion, first_emotion, second_emotion)

print("prompt: ", base_prompt)


# instantiate gpt3 model
gpt = gpt3()
# generate monologue
monologue = gpt.generate_monologue(prompt=base_prompt)
print("Generated Monologue:", monologue)