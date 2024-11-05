from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
ball = Ball()
scoreboard = Scoreboard()
while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.x_cor < -380:
        scoreboard.r_point()
    if ball.x_cor > 380:
        scoreboard.l_point()
    if ball.touch_paddle(l_paddle) or ball.touch_paddle(r_paddle):
        ball.increasing_speed()
        ball.bounce_y()
    if ball.out_of_area():
        ball.reset_position()
screen.exitonclick()
