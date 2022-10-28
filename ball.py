from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.6)
        self.color('LightBlue1')
        self.penup()
        self.x_move = -0.9
        self.y_move = 3

    def move(self):
        x_pose = self.xcor() + self.x_move
        y_pose = self.ycor() + self.y_move
        self.goto(x_pose, y_pose)

    def bounce_down(self):
        if self.distance(self.xcor(), 294) < 15:
            self.x_move *= 1.11
            self.y_move *= -1.03
            self.move()

    def bounce_up(self):
        if self.distance(self.xcor(), -285) < 15:
            self.x_move *= 1.11
            self.y_move *= -1.03
            self.move()

    def bounce_paddle(self):
        self.x_move *= -1
        self.move()




