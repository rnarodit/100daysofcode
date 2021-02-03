from turtle import Turtle, Screen
import random

#python tuple data type that looks like -> my tuple = (1,3,8)
# to access element in the tupple -> my_tupple[0]
# you cannot change the values in a tupple unlike a list
# you cannot remove, or add values to a tupple
# a tupple is immutable 
# you can convert tupple into a list -> list (my_tupple)

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

screen = Screen ()
screen.colormode(255)
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")


for i in range (0,100):
    timmy_the_turtle.pencolor(randomColor())
    timmy_the_turtle.forward(30)
    choosedirection(timmy_the_turtle) 

screen.exitonclick()




