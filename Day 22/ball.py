from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color ("white")
        self.ball_speed = 10 
        #self.setheading(35)
   
    def reset (self):
        self.goto(0,0)
        self.ball_speed = 10
    
    def  fast (self):
        self.ball_speed += 5 
    
    def move (self, top_hit , right_hit ):
        
        if right_hit == False:
            new_x = self.xcor()+ self.ball_speed
        else:
            new_x = self.xcor() - self.ball_speed 
        
        if(top_hit == True):
            new_y= self.ycor () - self.ball_speed
        else:
            new_y= self.ycor () + self.ball_speed
       
        self.goto(new_x,new_y)
