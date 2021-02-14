from turtle import Turtle 
from player import Player 
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.move_speed=STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if (random_chance == 1):
            new_car= Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len = 2 )
            new_car.color(random.choice(COLORS))
            starting_y = random.randint(-250, 250)
            new_car.goto(300, starting_y)
            self.all_cars.append(new_car)
    def level_up (self):
        self.move_speed += MOVE_INCREMENT 
        self.move_speed *= 0.9 
    def move (self):
        for car in self.all_cars:
            car.backward(self.move_speed)
    def collision (self , player):
        for car in self.all_cars :
            if (car.distance(player) < 30):
                return True 
        
    
