from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800 , height= 600)
screen.bgcolor ("black")
screen.title("Pong !")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball ()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down ,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down ,"s")


game_is_on = True
topWallHit = False
bottomWallHit = False
hit_right = False
while game_is_on :
    time.sleep(0.1)
    screen.update() 
    if ( ball.ycor() > 280) :
        topWallHit = True
    
    elif (ball.ycor()< -280):
        topWallHit = False
    
    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        hit_right = True
        ball.fast()
    
    elif ball.distance(l_paddle) < 50 and ball.xcor() <-320 :
        hit_right = False
        ball.fast()
    
    elif not ball.distance(r_paddle) < 50 and ball.xcor() > 380:
        hit_right = True
        scoreboard.score_l()
        ball.reset ()
    
    elif not ball.distance(l_paddle) < 50 and ball.xcor() <-380 :
        hit_right = False
        scoreboard.score_r()
        ball.reset ()
    
    ball.move(topWallHit, hit_right)

screen.exitonclick()