import random
import json

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

