from turtle import Turtle
from ball import Ball
GAME_OVER = ('Creepster', 50, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('SlateGray2')
        self.penup()
        self.ht()
        self.setpos(-10, 250)


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.penup()
        self.ht()
        self.setpos(-10, 0)
        self.write('Game Over', False, align='center', font=GAME_OVER)
