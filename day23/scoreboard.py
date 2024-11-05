from turtle import Turtle

FONT = {"Courier", 24, "normal"}

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 280)
        self.level = 1
        self.hideturtle()
        self.update()
    def increase_level(self):
        self.level += 1
    def update(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)