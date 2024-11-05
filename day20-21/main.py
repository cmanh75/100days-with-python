from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

starting_position = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0)]

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
new_snake = Snake(starting_position)
new_food = Food()
new_scoreboard = Scoreboard()
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

while True:
    screen.update()
    if new_snake.eat_itself():
        new_scoreboard.restart()
        new_snake.restart(starting_position)
    time.sleep(0.1)
    old = (new_snake.segments[len(new_snake.segments) - 1].xcor(), new_snake.segments[len(new_snake.segments) - 1].ycor());
    new_snake.move()    
    if new_snake.head.distance(new_food) < 15:
        new_food.refresh()
        new_scoreboard.update()
        new_scoreboard.refresh()
        new_snake.add_to_segments(old)
    if new_snake.head.xcor() > 290 or new_snake.head.ycor() > 290 or new_snake.head.xcor() < -290 or new_snake.head.ycor() < -290:
        new_scoreboard.restart()
        new_snake.restart(starting_position)
screen.exitonclick() 
