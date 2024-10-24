from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.xcor = x_position
        self.ycor = y_position
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto((x_position, y_position))
        self.speed(0.09)
    def up(self):
        if self.ycor + 20 > 250:
            return
        self.ycor += 20
        self.goto((self.xcor, self.ycor))
    def down(self):
        if self.ycor - 20 < -250:
            return
        self.ycor -= 20
        self.goto((self.xcor, self.ycor))