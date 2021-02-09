from turtle import Turtle 
ALIGNMENT= "center"
FONT= ("Arial", 24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260 )
        self.score = 0
        self.write(f"Your score is {self.score}", align= ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align= ALIGNMENT, font=FONT)
    
    def update_score (self):
        self.score +=1
        self.clear()
        self.write(f"Your score is {self.score}", align= ALIGNMENT, font=FONT)
    