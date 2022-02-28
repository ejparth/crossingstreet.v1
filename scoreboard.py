from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 1
        self.scoreupdate()

    def scoreupdate(self):
        self.clear()
        self.write(f"Score = {self.level}", align="center", font=("Arial", 12, "normal"))

    def levelupdate(self):

        self.level += 1
        print(self.level)
        self.scoreupdate()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))
