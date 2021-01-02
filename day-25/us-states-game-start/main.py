import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
guesses = []

while len(guesses) < 50:
    answer_state = screen.textinput(title=f"{len(guesses)}/50 States Correct",
                                    prompt="What's another state's name?")
    if not answer_state:
        break
    answer_state = answer_state.title()
    if answer_state in states:
        guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# missed = list(set(states) - set(guesses))
missed = [state for state in states if state not in guesses]

new_data = pandas.DataFrame(missed)
new_data.to_csv("states_to_learn")
