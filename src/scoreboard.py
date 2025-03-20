from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}    High Score: {self.high_score}",
                   False, "center", font=("Arial", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}",
                   False, "center", font=("Arial", 16, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))

        self.goto(x=0, y=0)
        self.write("Game Over", False, "center", font=("Arial", 16, "normal"))

    def read_high_score(self):
        with open("high_score.txt", mode="r") as file:
            return int(file.read())
