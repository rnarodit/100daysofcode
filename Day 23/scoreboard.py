from turtle import Turtle 
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0 
        self.goto (-220 , 250)
        self.update_score()
    
    def update_score(self):
        self.write(f"level: {self.level}", align = "center", font = FONT )

    def win(self):
        self.level +=1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align = "center", font = FONT )
