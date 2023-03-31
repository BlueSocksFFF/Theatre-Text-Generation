from languageModels.GPT3_5gen import gpt3_5_monologue_generator as gpt3_5
import languageModels.introduction_gen
from languageModels.introduction_gen import gpt3_5_introduction_generator as intro_bot
from helpers import blindline_prompt_setter



##setting up the show with an introduction of the game, give names of the improvisers playing

languageModels.introduction_gen.blind_line_intro(["mike, sarah, jack"], )

##blind_type = input() # grabbed from listening to audience

blindline_module = blindline_prompt_setter()
blindline_prompt = blindline_module.get_line_prompt()

print(blindline_prompt)


gpt = gpt3_5()

# generate monologue
line = gpt.generate_monologue(prompt=blindline_prompt)

print(line)
