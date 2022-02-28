from turtle import Screen
from player import Player
import time
from carmanager import Cars
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Let's Cross")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.upy, "Up")
sb = Scoreboard()
cars = Cars()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.gotonew()

    for carry in cars.all_cars:
        if carry.distance(player) < 20:
            sb.gameover()
            game_is_on = False

    if player.finish_line():
        sb.levelupdate()
        cars.speedup()

screen.exitonclick()
