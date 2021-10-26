import time
from turtle import Screen
from padle import Paddle
from ball import Ball
from scorebord import Scoreboard

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My PONG Game")
screen.tracer(0)

paddle1 = Paddle()
paddle1.set_player(1)
paddle2 = Paddle()
paddle2.set_player(2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

screen.onkey(paddle2.up, "o")
screen.onkey(paddle2.down, "k")

game_speed = 0.05
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    # paddle1.move()
    # paddle2.move()
    ball.move()

    if paddle1.ycor() > 250:
        print(paddle1.ycor())
        paddle1.rebound()
    elif paddle1.ycor() < -250:
        paddle1.rebound()

    if paddle2.ycor() > 250:
        paddle2.rebound()
    elif paddle2.ycor() < -250:
        paddle2.rebound()

    if ball.ycor() > 280:
        ball.rebound_y()
    elif ball.ycor() < -280:
        ball.rebound_y()
    if (ball.xcor() > 530 or ball.xcor() < -530) and (ball.distance(paddle1) < 50 or ball.distance(paddle2) < 30):
        ball.rebound_x()
        if game_speed > 0.01:
            game_speed -= 0.01
    if ball.xcor() > 600:
        ball.reset_position()
        scoreboard.increase_score1()
        game_speed = 0.1
    if ball.xcor() < -600:
        ball.reset_position()
        scoreboard.increase_score2()
        game_speed = 0.1
    if scoreboard.player1_score == 3 or scoreboard.player2_score == 3:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
