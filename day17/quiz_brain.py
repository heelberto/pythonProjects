class QuizBrain:
    def __init__(self, _question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = _question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (true/false): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, _user_answer, _correct_answer):
        if _user_answer.lower() == _correct_answer.lower():
            self.score += 1
            print("Answer correct")
        else:
            print("That's wrong")
        print(f"Correct answer: {_correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
