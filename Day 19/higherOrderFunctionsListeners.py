from turtle import Turtle,Screen
tim = Turtle()
screen = Screen ()

def move_forwards () :
    tim.forward(10)
screen.listen() # listen for events
#below we have a function being used as input for another function function_a(function_b) -> no need parenthesis 
#higher order function -> a function that can take another function as an input and work with its body
screen.onkey(key = "space", fun = move_forwards) # listen to a key press, needs a function to do something and a specified key. we do not use paranthesis if a function is used as an arugement like in move_forwards in this case 
# use keyword arguments in function u did not create yourself -> best practice
screen.exitonclick ()