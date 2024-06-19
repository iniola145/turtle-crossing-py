from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def generate_random_color(car):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    car.color(r, g, b)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.speed = 5

    def create_cars(self):
        car = Turtle("square")
        car.penup()
        car.setheading(180)
        random_y_axis = random.randint(-250, 250)
        car.goto(300, random_y_axis)
        car.turtlesize(1, 2)
        generate_random_color(car)
        self.all_cars.append(car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(self.speed)

    def increment(self):
        self.speed += 10

    def end_game(self):
        self.penup()
        self.home()
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))