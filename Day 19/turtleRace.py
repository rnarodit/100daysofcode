from turtle import Turtle, Screen
import random

screen = Screen ()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race , Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []

is_race_on = False
for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle" )
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto (x = -230, y = positions[turtle_index] )
    all_turtles.append (new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if (turtle.xcor () >= 230):
            is_race_on = False
            winnin_color = turtle.pencolor ()
            if winnin_color == user_bet:
                print (f"You've won! the{winnin_color} turtle is the winner !")
            else:
                print (f"You've lost! The {winnin_color} turtle is the winner !")
        random_distance = random.randint(0,10)
        turtle.forward (random_distance)
        


screen.exitonclick()