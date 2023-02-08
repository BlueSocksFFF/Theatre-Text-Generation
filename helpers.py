
def set_one_word_prompt(old_prompt, new_prompt):
    
    with open(r'prompts.txt', 'r') as file:
        data = file.read()
        data = data.replace(old_prompt, new_prompt)

    with open(r'prompts.txt', 'w') as file:
        file.write(data)
        
    print(old_prompt, " replaced with ", new_prompt)


