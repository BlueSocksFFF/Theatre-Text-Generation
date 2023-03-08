# -*- coding: utf-8 -*-

from languageModels.GPT3gen import gpt3_monologue_generator as gpt3
from languageModels.GPT3_5gen import gpt3_5_monologue_generator as gpt3_5
from api_client import write_to_api, append_to_api, read_from_api
from detect_key_phrases import key_phrase_extractor
from sentiment_analysis import sentiment_analyzer


# hardcoded audience suggestion, will pull from API later
raw_audience_speech = "huh well, the best day I have had was hiking the Himalayas with my friends"
print('raw audience suggestion', raw_audience_speech)

# testing sentiment analyzer, not integrated in the app yet
# instantiate sentiment_analyzer
sentiment_analysis_module = sentiment_analyzer()
sentiment, sentiment_score = sentiment_analysis_module.get_sentiment(text=raw_audience_speech)
targeted_sentiment = sentiment_analysis_module.get_targeted_sentiment(text=raw_audience_speech)
print(f"sentiment: {sentiment}")
print(sentiment_score)
print("targeted sentiment: ")
print(targeted_sentiment)

# instantiate the key_phrase_extractor
key_phrase_extraction_module = key_phrase_extractor()
key_phrases = key_phrase_extraction_module.get_key_phrases(text=raw_audience_speech)
# join the key words with "and"
parsed_key_phrases = " and ".join(key_phrases)
# prompt with keywords
prompt = f"Write a monologue based on {parsed_key_phrases}. It should be on the spot, a personal story that flits from topic to topic."
print("NEW PROMPT:", prompt)

# instantiate gpt3.5turbo model
gpt = gpt3_5()
# generate monologue
monologue = gpt.generate_monologue(prompt=prompt)
print("Generated Monologue:", monologue)

# sending that monologue to the API
write_to_api(monologue, "avatar_text")
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




