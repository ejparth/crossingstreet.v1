from turtle import Turtle

carspeed = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Green")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
        self.carspeed = 10

    def upy(self):
        self.forward(10)

    def finish_line(self):
        if self.ycor() > 280:
            self.goto(0, -280)
            return True



