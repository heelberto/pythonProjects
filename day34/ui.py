from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        # set up background
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # set up the score label
        self.score_label = Label(text="Score: 0", font=("Arial", 10, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # set up the white text box
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some Question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "bold"),
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # set up the true button
        true_button = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        # set up the false button
        false_button = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)
        # self.get_next_question()

    def false_pressed(self):
        is_false = self.quiz.check_answer(False)
        self.give_feedback(is_false)
        # self.get_next_question()

    def give_feedback(self, value):
        if value:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

