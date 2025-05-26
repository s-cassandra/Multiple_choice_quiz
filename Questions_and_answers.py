# Define a class to represent each quiz question and its correct answer
class Questions_and_answers:
    def __init__(self, prompt, answer):
        self.prompt = prompt    # Will contain the question text
        self.answer = answer    # Will contain the correct answer (e.g., 'a', 'b', 'c')
