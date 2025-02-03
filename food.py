from turtle import Turtle
from random import randint
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(name= "circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.generatefood()

    def generatefood(self):
        randomx = randint(-200,200)
        randomy = randint(-200,200)
        self.goto(randomx, randomy)
