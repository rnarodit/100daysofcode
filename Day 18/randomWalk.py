from turtle import Turtle, Screen
import random

def choosedirection (turtle):
    directions = [0, 90, 180, 270]
    direction = random.choice(directions)
    turtle.setheading(direction)

timmy_the_turtle = Turtle ()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

screen = Screen ()
screen.colormode(255)
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")


for i in range (0,100):
    timmy_the_turtle.pencolor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    timmy_the_turtle.forward(30)
    choosedirection(timmy_the_turtle)

screen.exitonclick()




