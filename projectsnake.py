from turtle import Screen
from classsnake import snake
from food import food
from scoreboard import scoreboard
from end import endgame
import time
myscreen = Screen()
myscreen.bgcolor('black')
myscreen.setup(width = 800, height = 600)
myscreen.title('Snake game')
myscreen.tracer(0)
gameison = True
mysnake = snake()
myscreen.listen()
myscreen.onkey(mysnake.moveup, "i")
myscreen.onkey(mysnake.movedown, "k")
myscreen.onkey(mysnake.moveleft, "l")
myscreen.onkey(mysnake.moveright, "j")
myfood = food()
myscoreboard = scoreboard()
myendgame = endgame()

while gameison:
    myscreen.update()   
    time.sleep(0.1)
    mysnake.move()
    if mysnake.segments[0].distance(myfood.xcor(), myfood.ycor())<15:
        myfood.generatefood()
        loop = False
        while loop:
            myfood.generatefood()
            for i in mysnake.segments:
                if i.distance(myfood.xcor(), myfood.ycor())<15:
                    exit()
                if mysnake.segments[len(mysnake.segments)-1].distance(myfood.xcor(), myfood.ycor()) >15:
                    loop = False
        mysnake.grow()
        myscoreboard.update_score()
    if mysnake.segments[0].xcor() > 390 or mysnake.segments[0].xcor() < -390 or mysnake.segments[0].ycor() > 290 or mysnake.segments[0].ycor() < -290:
        gameison = False
        myendgame.end()
    for segment in mysnake.segments[1:]:
        if mysnake.segments[0].distance(segment.xcor(), segment.ycor())<10:
           gameison = False
           myendgame.end()
        
    
myscreen.exitonclick()