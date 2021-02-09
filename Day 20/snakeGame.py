from turtle import Turtle , Screen # note we can remove the turtle class at this point since we used it for our food and snake classes 
from snake import Snake 
from scoreboard import Scoreboard
from food import Food
import time
screen = Screen()
screen.setup( width=600, height = 600)
screen.bgcolor("black")
screen.title("Sneeky Snake")
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(new_snake.up,"Up")
screen.onkey(new_snake.down ,"Down")
screen.onkey(new_snake.left ,"Left")
screen.onkey(new_snake.right, "Right")


# x_cord = [0 , -20, -40]
# for i in range (0,3):
#     snake_body.append(Turtle("square"))
#     snake_body[i].color("white")
#     snake_body[i].penup()
#     snake_body[i].goto(x_cord[i],0)

game_is_on = True
while(game_is_on):  
    screen.update()
    time.sleep(0.1)
    new_snake.snake_forward()
    #detect collision with food 
    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.extend ()
        scoreboard.update_score()
    #Detect collision with wall
    if new_snake.head.xcor() > 280 or new_snake.head.xcor()  < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor()< -280:
        game_is_on = False
        scoreboard.game_over()
    
    #Detect Collision With Tail
    for segment in new_snake.snake_body[1:] :
        # if segment == new_snake.head: 
        #     pass
        
        if  new_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    # for seg_num in range(len(snake_body)-1 , 0, -1):
    #     new_x = snake_body[seg_num-1].xcor()
    #     print(new_x)
    #     new_y = snake_body[seg_num-1].ycor()
    #     print(new_y)
    #     snake_body[seg_num].goto(new_x, new_y)
    # snake_body[0].forward(20)

    




screen.exitonclick ()