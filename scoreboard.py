from turtle import Turtle

with open("Highscore.txt", "r") as h:
    HIGHSCORE = int(h.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = HIGHSCORE
        self.write(arg=f"Score:{self.score}   HighScore:{self.high_score}", align="center")

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:{self.score}   HighScore:{self.high_score}", align="center")

    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Highscore.txt", "w") as h:
                h.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(arg=f"Score:{self.score}   HighScore:{self.high_score}", align="center")




 


