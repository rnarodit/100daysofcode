from turtle import Turtle, Screen # can import everything from the module with the following syntax -> from turtle import *  -> you won't have to do class.method () to call on a method and you will call on the method directly -> this syntax is not often used
import heroes
# if you import the turtle module with no specific class to create a new object u need to use the following syntax  -> new_turtle = turtle.Turtle()
# you can also give a module an Alias name -> import turtue as t  -> then us that alias -> tim = t.Turtle ()
# some modules u have to install first and can't import w/o installing .  
timmy_the_turtle = Turtle ()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.forward (100)
timmy_the_turtle.right(90)
print(heroes.gen ())





screen = Screen ()
screen.exitonclick()

