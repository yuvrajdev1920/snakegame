from turtle import Turtle,Screen

class Snake:
    def __init__(self):
        self.snake=[]
        self.start()
        
        # self.game_over=False

    def create_snake_cell(self):
        snake_cell=Turtle()
        snake_cell.shape("square")
        snake_cell.color("white")
        return snake_cell
    
    def start(self):
        for i in range(3):
            self.snake.append(self.create_snake_cell())
            for j in range(0,i):
                self.snake[i].penup()
                self.snake[i].backward(20)

    def extend(self, initial_pos):
        self.snake.append(self.create_snake_cell())
        self.snake[-1].penup()
        self.snake[-1].setposition(initial_pos)
    
    def move(self):
        i=len(self.snake)-1
        initial_pos=self.snake[i].pos()
        while(i>0):
            self.snake[i].penup()
            self.snake[i].setposition(self.snake[i-1].pos())
            i -= 1
        self.snake[0].penup()
        self.snake[0].forward(20)
        return initial_pos

    
