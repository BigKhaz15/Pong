from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.penup()
        self.goto(x= x_position, y= 0)

    def up(self):
        new_y_cor = self.ycor() + 30
        self.goto(x= self.xcor(),y= new_y_cor)

    def down(self):
        new_y_cor = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_y_cor)

    def paddle_reset(self, x_position):
        self.goto(x= x_position, y= 0)