import turtle
from turtle import *
import random

tim = Turtle()

distance = 90
tim.width(1)
tim.speed(0)
turtle.colormode(255)

colors = ["navy", "dark green", "firebrick", "thistle", "medium violet red", "spring green", "yellow", "black",
          "saddle brown"]

def random_color(_colors):
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    rand_color = (r, g, b)
    return rand_color

angle = 1

while angle < 361:
    tim.color(random_color(colors))
    tim.circle(100)
    tim.setheading(angle)
    angle += 3

screen = Screen()
screen.exitonclick()
