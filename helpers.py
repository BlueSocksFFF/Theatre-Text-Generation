import random
import json

# sets emotional arc for a monologue by providing two random emotions

class emotion_setter:
    def __init__(self):
        with open('emotions.json', 'r') as f:
            self.emotions = json.load(f)

        selected_emotion = random.choice(list(self.emotions.keys()))
        self.first_emotion = random.choice(self.emotions[selected_emotion])

        selected_emotion = random.choice(list(self.emotions.keys()))
        self.second_emotion = random.choice(self.emotions[selected_emotion])

    def get_emotions(self):
        return str(self.first_emotion), str(self.second_emotion)
    
class blindline_prompt_setter:
    def __init__(self):
        with open('blindline.json', 'r') as f:
            self.prompts = json.load(f)

        selected_prompt = random.choice(list(self.prompts.keys()))
        self.blindline_prompt = random.choice(self.prompts[selected_prompt])

    def get_line_prompt(self):
        return str(self.blindline_prompt)


