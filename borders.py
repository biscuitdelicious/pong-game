from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('RosyBrown2')
        self.shapesize(stretch_wid=0.3, stretch_len=39)
        self.penup()

