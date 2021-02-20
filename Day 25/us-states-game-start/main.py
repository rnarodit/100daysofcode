import turtle
import pandas

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
data = pandas.read_csv("Day 25/us-states-game-start/50_states.csv")
correct_guess =[]
screen = turtle.Screen()
screen.title("U.S States Game")
image="Day 25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = data["state"].tolist()

while (len(correct_guess)<50):
    answer_state = screen.textinput(title= f"{len(correct_guess)}/50 Correct", prompt = "What's another state's names ?").title()
    if answer_state == "Exit":
        states_to_learn =[state for state in states if state not in correct_guess] # for explanation of this look at day 26
        # for state in states :
        #     if not state in correct_guess:
        #         states_to_learn.append (state)

        state_data = {
            "states To Learn": states_to_learn
        }
        new_data= pandas.DataFrame(state_data)
        new_data.to_csv("Day 25/us-states-game-start/states_to_learn.csv")
        break
    if not (answer_state in correct_guess):
        if (answer_state in states):
            x_cor = int(data.x[data.state == answer_state ])
            y_cor = int(data.y[data.state == answer_state ])
            writer.goto(x_cor, y_cor)
            writer.write(f"{answer_state}")
            correct_guess.append(answer_state)



