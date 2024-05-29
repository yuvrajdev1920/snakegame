from turtle import Screen
from snake import Snake
from snakefood import Food  
from scoreboard import ScoreBoard
import time

def move_up():
    if(snake_obj.snake[0].heading() != 270.0):
        snake_obj.snake[0].setheading(90)

def move_down():
    if(snake_obj.snake[0].heading() != 90.0):
        snake_obj.snake[0].setheading(270)

def move_left():
    if(snake_obj.snake[0].heading() != 0.0):
        snake_obj.snake[0].setheading(180)

def move_right():
    if(snake_obj.snake[0].heading() != 180.0):
        snake_obj.snake[0].setheading(0)

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

snake_obj=Snake()
food=Food()
sb = ScoreBoard()

game_over=False
food_item=food.create_food()
while (not game_over):
    screen.update()
    time.sleep(0.1)
    initial_pos=snake_obj.move()
    if(snake_obj.snake[0].xcor()>290 or snake_obj.snake[0].xcor()<-300 or snake_obj.snake[0].ycor()>300 or snake_obj.snake[0].ycor()<-290):
        sb.game_over_msg()
        game_over=True
    if(snake_obj.snake[0].distance(food_item)<15):
        sb.update_score()
        food_item = food.eat_food(food_item)
        snake_obj.extend(initial_pos)
    for i in range(1,len(snake_obj.snake)):
        if(snake_obj.snake[0].distance(snake_obj.snake[i])<10):
            sb.game_over_msg()
            game_over=True
            break

print(f"Your score is {sb.score}.")
screen.exitonclick()