from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left",font=("Courier",20,"normal"))

    def increase_level(self):
        self.level += 1
        self.update()