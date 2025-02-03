from turtle import Turtle
class snake():
    def __init__(self):
        self.segments = []
        pos = [(0,0) , (-20,0), (-40,0)]
        for i in pos:
            newsegment = Turtle()
            newsegment.shape('square')
            newsegment.color('white')
            newsegment.penup()
            newsegment.goto(i)
            self.segments.append(newsegment)
        self.segments[0].color('yellow')
    def move(self):   
        for i in range(len(self.segments)-1, 0, -1):
            coor = [self.segments[i-1].xcor(), self.segments[i-1].ycor()]
            self.segments[i].goto(coor)
        self.segments[0].forward(20)
    def moveup(self):    
        if self.segments[0].heading() != 270:
           self.segments[0].setheading(90)
    def moveright(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def movedown(self):    
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def moveleft(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def grow(self):
        tempx = self.segments[len(self.segments)-1].xcor()
        tempy = self.segments[len(self.segments)-1].ycor()
        i = [tempx , tempy]
        self.move()
        newsegment = Turtle()
        newsegment.shape('square')
        newsegment.color('white')
        newsegment.penup()
        newsegment.goto(i)
        self.segments.append(newsegment)