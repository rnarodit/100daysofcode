from turtle import Turtle
UP= 90
DOWN = 270 
class Paddle (Turtle):
    def __init__ (self, coordinates):
        super().__init__()
        #self.hideturtle()
        self.shape("square")
        self.penup()
        #self.setheading(90)
        self.shapesize(stretch_wid= 5, stretch_len = 1)
        self.color("white")
        self.setposition(coordinates)
        #self.showturtle()
    
    
   
    def up(self):
        self.sety(self.ycor()+20)
        
    def down(self):
        self.sety(self.ycor()-20)