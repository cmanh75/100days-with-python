import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

reveal = turtle.Turtle()
reveal.hideturtle()
reveal.penup()
data = pandas.read_csv("day25/50_states.csv")
all_states = data.state.to_list()

correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_states:
                missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv("day25/start_to_learn.csv")
        break
    if answer_state in all_states:
        correct_states.append(answer_state)
        correspond_state = data[data.state == answer_state]
        reveal.goto(correspond_state.x.item(), correspond_state.y.item())
        reveal.write(answer_state)
screen.exitonclick()