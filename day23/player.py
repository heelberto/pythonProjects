from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)