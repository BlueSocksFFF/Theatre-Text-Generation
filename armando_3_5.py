from languageModels.GPT3_5gen import gpt3_5_monologue_generator as gpt3_5
import languageModels.introduction_gen
from languageModels.introduction_gen import gpt3_5_introduction_generator as intro_bot
import json
import random
from detect_key_phrases import key_phrase_extractor
from sentiment_analysis import sentiment_analyzer
from detect_entity import entity_extractor
from emotions import emotion_setter


##setting up the show with an introduction of the improvisers

languageModels.introduction_gen.basic_intro()


# audience word suggestion
suggestion = "wind"

 ### MONOLOGUE ONE ####

# setting new emotions for the monologue
emotion_set_module = emotion_setter()
first_emotion, second_emotion = emotion_set_module.get_emotions()

print(first_emotion, second_emotion)

base_prompt = "Write a monologue that discusses {}. This monologue should sound like it was made up on the spot. Use multiple personal anecdotes, filler words like 'ah' 'um' or 'like', rhetorical questions, and varied sentence length. Do not begin with a filler word. I want a natural tone and feeling. The monologue should begin with the emotion {} and end with the emotion {}.".format(suggestion, first_emotion, second_emotion)

print("prompt: ", base_prompt)

gpt = gpt3_5()
# generate monologue
first_monologue = gpt.generate_monologue(prompt=base_prompt)

print(first_monologue)

 #################

 ### MONOLOGUE TWO ####

#analyze the first monologue with sentiment and key phrases

# instantiate sentiment_analyzer
sentiment_analysis_module = sentiment_analyzer()
sentiment, sentiment_score = sentiment_analysis_module.get_sentiment(text=first_monologue)
print(f"sentiment: {sentiment}")
print(sentiment_score)

# instantiate the key_phrase_extractor
key_phrase_extraction_module = key_phrase_extractor()
key_phrases = key_phrase_extraction_module.get_key_phrases(text=first_monologue)
print("key phrases: ", key_phrases)

second_base_prompt = "Write a monologue that has a {} tone. This monologue should sound like it was made up on the spot. Use multiple personal anecdotes, filler words like 'ah' 'um' or 'like', rhetorical questions, and varied sentence length. Do not begin with a filler word. I want a natural tone and feeling. Incorporate some ideas from this list {}.".format(sentiment, key_phrases)


gpt = gpt3_5()
# generate monologue
second_monologue = gpt.generate_monologue(prompt=second_base_prompt)

print(second_monologue)




