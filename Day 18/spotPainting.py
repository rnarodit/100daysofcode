import colorgram 
from turtle import Turtle, Screen
import random

# colors = colorgram.extract (r"C:\Users\ron\Documents\repos\100daysofcode\Day 18\image.jpg" , 30)
# color_list = []
# for color in colors:
#     rgb = (color.rgb[0],color.rgb[1],color.rgb[2])
#     color_list.append(rgb)
# print (color_list)




#def randomColor ():
#     r = random.randrange(0,255)
#     g = random.randrange(0,255)
#     b = random.randrange(0,255)
#     return (r,g,b) # returning a tupple

# def choosedirection (turtle):
#     directions = [0, 90, 180, 270]
#     direction = random.choice(directions)
#     turtle.setheading(direction)

timmy_the_turtle = Turtle ()
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.setx (-200)
timmy_the_turtle.sety (-200)
timmy_the_turtle.speed("fastest")
screen = Screen ()
screen.colormode(255)
color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 
227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31)]
def draw_row ():
    for i in range (0, 10):
        timmy_the_turtle.dot(15, random.choice(color_list))
        timmy_the_turtle.forward(50)
        

x_origin = timmy_the_turtle.xcor()
y_origin = timmy_the_turtle.ycor ()

for i in range (0,10):
    draw_row ()
    y_origin += 50
    timmy_the_turtle.setx(x_origin)
    timmy_the_turtle.sety (y_origin)

screen.exitonclick()