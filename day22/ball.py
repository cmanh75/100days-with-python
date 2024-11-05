from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_cor = 0
        self.y_cor = 0
        self.x_dir = 1
        self.y_dir = 1
        self.move_speed = 0.1
        self.color("white")
        self.shape("circle")
        self.penup()
    def bounce_x(self):
        self.y_dir *= -1
    def bounce_y(self):
        self.x_dir *= -1
    def touch_paddle(self, paddle):
        if self.x_cor < 350 and self.distance(paddle) < 60 and self.x_dir == 1 and abs(self.x_cor - 350) < 15:
            return True
        if self.x_cor > -350 and self.distance(paddle) < 60 and self.x_dir == -1 and abs(self.x_cor + 350) < 15:
            return True
        return False
    def increasing_speed(self):
        self.move_speed *= 0.9
    def out_of_area(self):
        if self.x_cor < -380 or self.x_cor > 380:
            return True
        return False
    def reset_position(self):
        self.x_cor = 0
        self.y_cor = 0
        self.move_speed = 0.1
        self.bounce_x()
    def move(self):
        new_x = self.x_cor + self.x_dir * 10
        new_y = self.y_cor + self.y_dir * 10
        if new_y > 280 or new_y < -280:
            self.bounce_x()
            self.move()
        self.x_cor = new_x
        self.y_cor = new_y
        self.goto(self.x_cor, self.y_cor)