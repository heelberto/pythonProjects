from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    cur_question = Question(question_text,question_answer)
    question_bank.append(cur_question)

# for question in question_bank:
#     print(f"Text: {question.text}\nAnswer: {question.answer}")

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()