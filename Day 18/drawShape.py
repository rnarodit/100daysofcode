from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle ()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

screen = Screen ()
screen.colormode(255)
for i in range (3,11):
    deg = 360 / i
    sides = i
    timmy_the_turtle.pencolor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    for j in range (0,sides):
        timmy_the_turtle.forward (100)
        timmy_the_turtle.right(deg)

screen.exitonclick()




