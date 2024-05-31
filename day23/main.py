from player import Player
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=player.move_backward, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect for collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()
