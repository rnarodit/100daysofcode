from turtle import Turtle, Screen
import random

def randomColor ():
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    return (r,g,b) # returning a tupple

def choosedirection (turtle):
    directions = [0, 90, 180, 270]
    direction = random.choice(directions)
    turtle.setheading(direction)

timmy_the_turtle = Turtle ()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.speed("fastest")
screen = Screen ()
screen.colormode(255)




def draw_spyrogrpah (gap_size):
    for i in range (int(360 / gap_size)):
        timmy_the_turtle.pencolor(randomColor())
        timmy_the_turtle.circle(100) 
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+gap_size)
draw_spyrogrpah(5)

screen.exitonclick()