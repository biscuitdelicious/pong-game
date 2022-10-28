from turtle import Turtle
POSITIONS_A = (-385, 0)
POSITIONS_B = (375, 0)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('khaki1')
        self.shapesize(stretch_wid=4, stretch_len=0.4)
        self.penup()

    def go_up(self):
        y_pose = self.ycor() + 30
        self.goto(self.xcor(), y_pose)

    def go_down(self):
        y_pose = self.ycor() - 30
        self.goto(self.xcor(), y_pose)


class PaddleA(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(POSITIONS_A)


class PaddleB(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(POSITIONS_B)
