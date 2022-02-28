from turtle import Turtle
from random import randint, choice

list_color = ["red", "green", "blue", "yellow", "violet"]


class Cars:
    def __init__(self):
        self.all_cars = []
        self.carspeed = 5

    def create_car(self):
        randdy = randint(1, 6)
        if randdy == 1:
            newcar = Turtle("square")
            newcar.shapesize(1, 2)
            newcar.color(choice(list_color))
            newcar.penup()
            YCOR = randint(-250, 250)
            newcar.goto(280, YCOR)
            newcar.setheading(180)
            self.all_cars.append(newcar)


    def gotonew(self):
        for car in self.all_cars:
            car.forward(self.carspeed)

    def speedup(self):
        self.carspeed += 5
        self.gotonew()