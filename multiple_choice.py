# Import the Questions_and_answers class from the other file
from Questions_and_answers import Questions_and_answers

# List of question strings with options
questions_prompts = [
    "What is the capital of England?\n(a) Manchester\n(b) London\n(c) Essex\n\n",
    "What is the capital of Japan?\n(a) Tokyo\n(b) Kyoto\n(c) Yokohama\n\n",
    "What is the capital of Sudan?\n(a) Kassala\n(b) Omdurman\n(c) Khartoum\n\n"
]

# Create a list of Questions_and_answers objects with correct answers
questions = [
    Questions_and_answers(questions_prompts[0], "b"),
    Questions_and_answers(questions_prompts[1], "a"),
    Questions_and_answers(questions_prompts[2], "c")
]

# Define a function to run the quiz
def run_test(questions):
    score = 0  # Initialise score

    # Loop through each question
    for question in questions:
        attempt = input(question.prompt)  # Ask the question and get user's answer
        if attempt == question.answer:    # Check if the answer is correct
            score += 1                    # Increment score if correct

    # Show the total score after the quiz ends
    print(f"You got {score}/{len(questions)} correct")

# Start the quiz
run_test(questions)
