from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

questions = question_data["results"]


for question in questions:
    """Esto itera sobre la lista de preguntas "results", crea objetos 
    questions en funcion de la clase Question y luego las agrega a la lista question bank"""
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")