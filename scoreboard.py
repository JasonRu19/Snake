from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as self.data:
            self.h_score = self.data.read()
        self.penup()
        self.hideturtle()
        self.goto(x = 0, y = 270)
        self.color("white")

    def show_scoreboard(self):
        self.write(f"Score: {self.score}     High Score: {self.h_score}", align=ALIGNMENT, font = FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}     High Score: {self.h_score}", align=ALIGNMENT, font = FONT)

    def high_score(self):
        if self.score > int(self.h_score):
            self.h_score = self.score
            with open("data.txt", "w") as self.data:
                self.data.write(str(self.h_score))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.h_score}", align=ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)


