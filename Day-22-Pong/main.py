from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = ScoreBoard()
ball = Ball()


#
# screen.listen()
# screen.onkey(r_paddle.go_up(),"Up")
# screen.onkey(r_paddle.go_down(),"Down")
# screen.onkey(l_paddle.go_up(),"w")
# screen.onkey(l_paddle.go_down(), "s")

# 终于找到问题了fun 做参数传进去的时候不用带括号，带括号就不管用了
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True

while game_on:
    screen.update()
    ball.move()
    time.sleep(0.01)

    # print(f"Ball position: ({ball.xcor()}, {ball.ycor()})")
    # print(f"R Paddle position: ({r_paddle.xcor()}, {r_paddle.ycor()})")
    # print(f"L Paddle position: ({l_paddle.xcor()}, {l_paddle.ycor()})")

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

