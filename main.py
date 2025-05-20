from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

paddle_1 = Paddle(350)
paddle_2 = Paddle(-350)
ball = Ball()

def reset_game():
    time.sleep(.5)
    ball.reset_ball(flip_x= False)
    scoreboard.reset_scoreboard()
    paddle_1.paddle_reset(350)
    paddle_2.paddle_reset(-350)

screen.listen()
screen.onkey(fun= paddle_1.up, key= "Up")
screen.onkey(fun= paddle_1.down, key= "Down")
screen.onkey(fun= paddle_2.up, key= "w")
screen.onkey(fun= paddle_2.down, key= "s")
screen.onkey(fun= reset_game, key= "r")


def play_game():
    reset_game()
    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(ball.move_speed)
        ball.bounce_y()

        #Detect collision with Paddle
        if ball.distance(paddle_1) < 55.0 and ball.xcor() > 320.0:
            ball.bounce_x()
            ball.increase_ball_speed()
        if ball.distance(paddle_2) < 55.0 and ball.xcor() < -320.0:
            ball.bounce_x()
            ball.increase_ball_speed()

        #Detect when paddle misses ball aka someone scores
        if ball.xcor() > 405.0:
            game_is_on = scoreboard.left_player_scores()
            ball.reset_ball(flip_x= True)
        if ball.xcor() < -405.0:
            game_is_on = scoreboard.right_player_scores()
            ball.reset_ball(flip_x= True)
play_game()
screen.exitonclick()
