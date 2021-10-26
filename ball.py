from turtle import Turtle
import random
MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.setheading(random.randint(0, 360))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebound_y(self):
        self.y_move *= -1

    def rebound_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.rebound_x()

