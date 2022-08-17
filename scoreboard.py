from msilib.schema import Font
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.view_score()

    def view_score(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}',
                   False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.view_score()

    def addscore(self):
        self.score += 1
        self.view_score()
