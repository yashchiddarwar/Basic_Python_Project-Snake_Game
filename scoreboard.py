from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, "center", ('Arial', 23, 'normal'))

    def score_updater(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Score: {self.score}", False, "center", ('Arial', 23, 'normal'))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, "center", ('Arial', 25, 'normal'))




