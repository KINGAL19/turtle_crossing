from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.penup()
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def check_arrive(self):
        if self.ycor() >= FINISH_LINE:
            return True
        return False
