import pandas
import turtle

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states =  data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name ?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    # Check if answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]


        t.goto(int(state_data.x), int(state_data.y))

        t.write(answer_state)
        # if they do get it right:
            # Need to create a turtle of text, and place it on the x, y position

