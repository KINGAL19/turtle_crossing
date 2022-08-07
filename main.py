import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.onkey(player.up, 'Up')
screen.listen()

cars_m = CarManager()
scoreboard = Scoreboard()

game_is_on = True
start = time.time()
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for _ in range(2):
        if len(cars_m.cars) < 2:
            cars_m.car_appear()
        elif cars_m.cars[-1].xcor() < 260:
            cars_m.car_appear()
    cars_m.move()

    for car in cars_m.cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.check_arrive():
        player.goto_start()

        cars_m.lever_up()
        scoreboard.increase_lever()

        if scoreboard.level > 10:
            game_is_on = False
end = time.time()
spend_time = end - start

scoreboard.show_score(round(spend_time, 2))
screen.update()


screen.exitonclick()