from turtle import Turtle


FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.write(f'Level: {self.level}', font=FONT)

    def refresh(self):
        self.clear()
        self.update()

    def increase_lever(self):
        self.level += 1
        self.refresh()

    def show_score(self, time):
        self.clear()
        self.home()
        self.write(f'Level: {self.level}', align='center', font=('Courier', 48, 'normal'))
        self.goto(0, -50)
        self.write(f'Spend: {time}s', align='center', font=('Courier', 48, 'normal'))
