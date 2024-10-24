import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

screen = Screen()

screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

ball = Ball()
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
time_increment = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # time_increment -= .005


    # detect when right paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        scoreboard.update_scoreboard()

    # detect when left paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        scoreboard.update_scoreboard()

screen.exitonclick()
