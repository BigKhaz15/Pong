from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x= 0, y= 0)
        self.x_move = random.choice([-10,10])
        self.y_move = random.choice([-10,10])
        self.move_speed = .1

    def move(self):
        self.goto(x= self.xcor()+self.x_move, y= self.ycor()+self.y_move)

    def bounce_y(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self, flip_x):
        self.move_speed = 0.1
        self.goto(x= 0, y= 0)
        self.y_move = random.choice([-10,10])
        if flip_x:
            self.bounce_x()
        else:
            self.x_move = random.choice([-10, 10])

    def increase_ball_speed(self):
        self.move_speed *= .9