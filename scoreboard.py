from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_player_score = 0
        self.r_player_score = 0
        self.update_scoreboard()
        self.winner = ""

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_player_score, align= "center", font= ("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_player_score, align= "center", font= ("Courier", 80, "normal"))

    def left_player_scores(self):
        self.l_player_score += 1
        self.update_scoreboard()
        if self.l_player_score == 5:
            self.winner = "Left Player"
            self.print_winner()
            return False
        else:
            return True
    def right_player_scores(self):
        self.r_player_score += 1
        self.update_scoreboard()
        if self.r_player_score == 5:
            self.winner = "Right Player"
            self.print_winner()
            return False
        else:
            return True

    def print_winner(self):
        self.goto(0,0)
        self.write(f"The winner is {self.winner}!", align="Center", font= ("Courier", 25, "bold"))

    def reset_scoreboard(self):
        self.l_player_score = 0
        self.r_player_score = 0
        self.winner = ""
        self.clear()
        self.update_scoreboard()