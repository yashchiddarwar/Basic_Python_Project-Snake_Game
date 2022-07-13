from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.high_score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ('Arial', 23, 'normal'))

    def score_updater(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ('Arial', 23, 'normal'))

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = -1
        self.score_updater()





