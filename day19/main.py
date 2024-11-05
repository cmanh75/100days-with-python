import turtle
import random

screen = turtle.Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
turtle_list = []
for turtle_index in range(0, 6):
    cmanh = turtle.Turtle(shape="turtle")
    cmanh.penup()
    cmanh.color(colors[turtle_index])
    cmanh.goto(-230, y_position[turtle_index])
    turtle_list.append(cmanh)
stop = False
while stop == False:
    for cmanh in turtle_list:
        cmanh.forward(random.randint(1, 10))
        if cmanh.xcor() > 230:
            if cmanh.pencolor() == user_bet:
                print(f"You've won! {cmanh.pencolor()} is the winner!")
            else:
                print(f"You've lose! {cmanh.pencolor()} is the winner!")
            stop = True
            break
screen.exitonclick()