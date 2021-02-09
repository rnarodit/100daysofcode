from turtle import Turtle
MOVE_DISTANCE = 20
POSITIONS = [(0,0) , (-20,0), (-40,0)]
UP= 90
DOWN = 270 
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake (self):
        for position in POSITIONS:
               self.add_segment(position)
    
    def add_segment (self ,position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snake_body.append(new_seg)
    
    def extend (self):
        self.add_segment(self.snake_body[-1].position()) # position () is method from the turtle class 

    def snake_forward(self):  
        for seg_num in range(len(self.snake_body)-1 , 0, -1):
            new_x = self.snake_body[seg_num-1].xcor()
            print(new_x)
            new_y = self.snake_body[seg_num-1].ycor()
            print(new_y)
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)