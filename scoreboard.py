from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 260)
        self.hideturtle()
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

