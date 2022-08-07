from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREAMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.movement = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.cars = []
        self.car_appear()

    def car_appear(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-270, 270))
            car.setheading(180)
            self.cars.append(car)


    def move(self):
        for car in self.cars:
            car.forward(self.movement)

    def lever_up(self):
        self.movement += MOVE_INCREAMENT

