
def set_one_word_prompt(old_prompt, new_prompt):
    
    with open(r'prompts.txt', 'r') as file:
        data = file.read()
        data = data.replace(old_prompt, new_prompt)

    with open(r'prompts.txt', 'w') as file:
        file.write(data)
        
    print(old_prompt, " replaced with ", new_prompt)


def compare_generators(prompt, *argv):
    for model in argv:
        model.generate(prompt)




def log_the_text(log_type, prompt, text):
    fo = open("generatedTexts/{}_generated_text.txt".format(log_type),"a")
    fo.write("\n{} from ".format(log_type) + prompt + ": " + text)
    fo.close()
    print("{}: ".format(log_type) + text)



def manage_prompt_wrappers(prompts, wrapper_num):
    file1 = open('prompts.txt', 'r')
    lines = file1.readlines()
    prompts.append(lines[wrapper_num])
    file1.close()
    



