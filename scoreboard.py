from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.score = 0
        self.write(f'CURRENT SCORE: {self.score}', 8, align='center', font=('Courier', 12, 'normal'))
    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f'CURRENT SCORE: {self.score}', 8, align='center', font=('Courier', 12, 'normal'))
