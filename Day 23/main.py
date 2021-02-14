import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard ()
screen.onkey(player.up, "Up" )

game_is_on = True
carMaker = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    
    if (car_manager.collision(player)):
        scoreboard.game_over()
        game_is_on = False
    
    if (player.finished()):
        player.reset()
        car_manager.level_up()
        scoreboard.win()
        
    
    
        

screen.exitonclick()