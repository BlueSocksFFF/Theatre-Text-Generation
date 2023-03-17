import multiprocessing

from languageModels.GPT3gen import gpt3_monologue_generator as gpt3
from languageModels.GPT3_5gen import gpt3_5_monologue_generator as gpt3_5

class monologue_generator:
    def __init__(self) -> None:
        self.GPT3 = gpt3()
        self.GPT35 = gpt3_5()

    def generate_monologue(self, prompt):
        result_queue = multiprocessing.Queue()

        p1 = multiprocessing.Process(target=self._generate_monologue, args=(self.GPT3, prompt, result_queue))
        p2 = multiprocessing.Process(target=self._generate_monologue, args=(self.GPT35, prompt, result_queue))

        p1.start()
        p2.start()

        result = result_queue.get()

        p1.terminate()
        p2.terminate()

        return result

    # helper method that executes the generator function in a separate process and puts the result into the result queue
    def _generate_monologue(self, model, prompt, result_queue):
        result = model.generate_monologue(prompt)
        result_queue.put(result)
