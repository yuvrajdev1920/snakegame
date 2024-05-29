from turtle import Turtle
import random

class Food:
    # def __init__(self):
        # self.create_food()

    def create_food(self):
        food = Turtle()
        food.penup()
        food.shape("circle")
        food.color("red")
        food.resizemode("user")
        food.shapesize(0.5,0.5,1)
        food.setposition(random.randint(-280,280),random.randint(-280,280))
        return food
    
    def eat_food(self, food):
        food.hideturtle()
        return self.create_food()