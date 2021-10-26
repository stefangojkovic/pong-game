from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.resizemode("user")
        self.setheading(UP)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("white")
        self.penup()

        # self.goto((-550, 0))

    def set_player(self, player):
        if player == 1:
            self.goto(-550, 0)
        elif player == 2:
            self.goto(550, 0)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        self.setheading(UP)
        if self.ycor() <= 250:
            self.move()

    #        self.move()

    def down(self):
        self.setheading(DOWN)
        if self.ycor() >= -250:
            self.move()

    #        self.move()

    def rebound(self):
        if self.ycor() > 250:
            self.setheading(DOWN)
        else:
            self.setheading(UP)
