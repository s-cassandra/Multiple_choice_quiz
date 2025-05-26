# Multiple_choice_quiz

This is a simple command-line quiz application built with Python. It presents multiple-choice questions to the user and evaluates their answers, giving a final score at the end.

## Features

- Stores questions and their corresponding answers using a custom class
- Accepts user input for each question
- Calculates and displays the user's score

## 📁 Project Structure

Multiple_choice_quiz
│
├── main.py # The main file that runs the quiz
├── Questions_and_answers.py # Contains the Questions_and_answers class
└── README.md # Project documentation


## 📝 How It Works

1. The `Questions_and_answers` class holds a single question and its correct answer.
2. A list of question prompts is created.
3. A list of `Questions_and_answers` instances is initialised using the prompts and correct answers.
4. The `run_test()` function loops through the questions, accepts user input, and compares it with the correct answer.
5. The user receives a score out of the total questions.
