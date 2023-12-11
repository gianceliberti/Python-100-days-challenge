from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

questions = question_data["results"]


for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")