class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
   

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False. )")
        self.check_answer(user_answer, current_question.answer)



    def check_answer(self, user_answer, correct_answer):
        user_answer_lower = user_answer.lower()  # Convierte la respuesta del usuario a minúsculas
        correct_answer_lower = correct_answer.lower()  # Convierte la respuesta correcta a minúsculas

        if user_answer_lower == correct_answer_lower:
            self.score += 1
            print("Correct")
        else:
            print("Wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")