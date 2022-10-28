# We need classes for: borders, score, player 1 board, player 2 board, ball
from turtle import Screen
from paddle import PaddleA, PaddleB
from ball import Ball
from borders import Border
from scoreboard import Scoreboard, GameOver

score_right = 0
score_left = 0
screen = Screen()
GAME_IS_ON = True

screen.tracer(0)
screen.bgcolor('gray30')
screen.setup(width=800, height=600)
screen.title('Pong game')

scoreboard = Scoreboard()  # Making the scoreboard
scoreboard.write('0 : 0', False, align='center', font=('Avenir', 20, 'bold'))


l_paddle = PaddleA()
r_paddle = PaddleB()
ball = Ball()

up_border = Border()  # Creating up border
down_border = Border()  # Creating down border

up_border.goto(-5, 290)
down_border.goto(-5, -280)

while GAME_IS_ON:
    screen.update()
    screen.listen()
    screen.onkeyrelease(r_paddle.go_up, 'Up')
    screen.onkeyrelease(r_paddle.go_down, 'Down')
    screen.onkeyrelease(l_paddle.go_up, 'w')
    screen.onkeyrelease(l_paddle.go_down, 's')
    ball.move()
    ball.bounce_down()
    ball.bounce_up()
    if ball.distance(r_paddle) < 24 and ball.xcor() > 330:  # Bouncing the ball right paddle
        ball.bounce_paddle()
        scoreboard.clear()
        score_right += 1
        scoreboard.write(f'{score_left} : {score_right}', False, align='center', font=('Avenir', 20, 'bold'))
    if ball.distance(l_paddle) < 24 and ball.xcor() < -365:  # Bouncing the ball left paddle
        ball.bounce_paddle()
        scoreboard.clear()
        score_left += 1
        scoreboard.write(f'{score_left} : {score_right}', False, align='center', font=('Avenir', 20, 'bold'))
    if ball.xcor() > 385 or ball.xcor() < -390:  # Checks if the ball gets outside
        GAME_IS_ON = False  # Turning off the game
        scoreboard = GameOver()  # Printing 'game over


screen.exitonclick()
