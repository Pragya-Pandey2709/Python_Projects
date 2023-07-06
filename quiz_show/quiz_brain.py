class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

'''
Certainly! This code appears to be a simplified implementation of a quiz game. Let's break it down step by step:

1. The code defines a class called `QuizBrain` that represents the brain or logic of the quiz game.

2. The `__init__` method is a special method called a constructor. It initializes the `QuizBrain` object with the following attributes:
   - `question_number`: Keeps track of the current question number.
   - `score`: Keeps track of the user's score (number of correct answers).
   - `question_list`: Stores the list of questions for the quiz.

3. The `still_has_questions` method checks if there are more questions remaining in the quiz. It returns `True` if the question number is less than the length of the question list, indicating that there are more questions to be asked.

4. The `next_question` method displays the next question to the user and collects their answer. It performs the following steps:
   - Retrieves the current question from the question list using the `question_number` as the index.
   - Increments the `question_number` by 1 to move to the next question.
   - Asks the user for their answer using the `input` function and displays the question using string formatting.
   - Calls the `check_answer` method to evaluate the user's answer.

5. The `check_answer` method compares the user's answer with the correct answer for the current question. It performs the following actions:
   - Converts both the user's answer and the correct answer to lowercase for case-insensitive comparison.
   - If the user's answer matches the correct answer, it increments the `score` by 1 and prints a message indicating the correct answer.
   - If the user's answer is incorrect, it prints a message indicating that the answer is wrong.
   - Prints the correct answer for the question.
   - Displays the user's current score and the number of questions answered so far.
   - Prints a newline character for formatting.

Overall, this code sets up the quiz, tracks the user's progress, asks questions one by one, and checks the user's answers to determine if they are correct.
'''
