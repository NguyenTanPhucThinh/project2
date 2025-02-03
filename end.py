from turtle import Turtle
class endgame(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 0)
    def end(self):
        self.write("Game Over", align = 'center', font=('Courier', 24, 'normal'))