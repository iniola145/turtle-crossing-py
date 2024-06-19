import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle.colormode(255)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# To move turtle
screen.listen()
screen.onkey(player.Up, "Up")

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter % 6 == 0:
        car_manager.create_cars()

    car_manager.move_cars()
    counter += 1

    # Check if there is collison between the turtle and any car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            car_manager.end_game()
            game_is_on = False

    # Check if player is at finish line
    if player.ycor() == 300:
        player.restart()
        car_manager.increment()
        scoreboard.next_level()

screen.exitonclick()
