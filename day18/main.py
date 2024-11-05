import turtle
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


cmanh = turtle.Turtle()
cmanh.speed("fastest")
cmanh.hideturtle()
cmanh.penup()
cmanh.setheading(225)
cmanh.forward(300)
cmanh.setheading(0)
for j in range(0, 10):
    for i in range(0, 10):
        cmanh.dot(20, random_color())
        cmanh.forward(42)
    cmanh.setheading(90)
    cmanh.forward(42)
    cmanh.setheading(180)
    for i in range(0, 10):
        cmanh.forward(42)
    cmanh.setheading(0)




screen = turtle.Screen()
screen.exitonclick()