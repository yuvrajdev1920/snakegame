from turtle import Turtle
from snake import Snake

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"SCORE: {self.score}", align="center")

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align="center")

    def game_over_msg(self):
        display = Turtle()
        display.hideturtle()
        display.color("white")
        display.write(f"GAME OVER!!! You scored {self.score}", align="center")
