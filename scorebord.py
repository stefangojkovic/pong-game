from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 50, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score1(self):
        self.player1_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score2(self):
        self.player2_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.player1_score} : {self.player2_score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.clear()
        if self.player1_score > self.player2_score:
            self.write(f"Player 1 wins by {self.player1_score}:{self.player2_score}", font=FONT, align=ALIGNMENT)
        else:
            self.write(f"Player 2 wins by {self.player1_score}:{self.player2_score}", font=FONT, align=ALIGNMENT)