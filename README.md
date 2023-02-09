# Theatre-Text-Generation

## General Langauges and Packages Required
Python == 3.10+


## Types of Language Models

GPT3gen.py is communicating with GPT-3's official API. 
- You can generate using this API by calling: $ python3 main.py gpt3_generator "PROMPT"

revChatGPTgen.py is accessing ChatGPT's API through unofficial means.
- You can generate using this API by calling: $ python3 main.py chatgpt_generator "PROMPT"
- having issues generating as of 11pm feb 8th

AI21 studio is using AI21's API access to Jurassic-1 large-language-models.
- You can generate using this API by calling: $ python3 main.py ai21_generator "PROMPT"


 possible others:
- GPT2
- Trying to access GPTNeo but requires pytorch which is incompatible with Python 3.10
- Bloom

#### Files

Main.py
 - utilizes whichever language model you direct it to. You must specify the language model when
  calling main.py 

  For example: $ python3 main.py chatgpt_generator zebra

 - You may also want to compare different language models using the same prompt. 
    To do so call: $ python3 main.py compare zebra

    This will use that same prompt "zebra" for (currently two) different language models.
    This result is published in "comparing_generators.txt"

 - Takes in a one word audience suggestion as its 3rd argument. You must give an audience suggestion when calling main.py

 - Can also be used to send text to the Avatar API. This will inherently use the GPT3 model.
    
    For example: $ python3 main.py avatar_api zebra

    This will generate a monologue based on zebra (wrapped in our prompt engineering to format as monologue) and send it to the Avatar team's API


helpers.py
- holds helper functions
- currently working on greater control over the prompt engineering with a "prompt wrapper" function


api_client.py
- communicates with the Avatar API

prompts.txt
- holds the necessary prompt engineering for our generators to create a monologue, the  PLACEHOLDER_PROMPT  is replaced by whichever audience suggestion is input by the user when main.py is run

gpt3_generated_text
- holds the text generated by gpt3 language model

chatgpt_generated_text
- holds the text generated by chatgpt language model



#### Installation
```
pip3 install revChatGPT

```

