from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.score = 0
        self.update_scoreboard()
        
        
        
    def update_scoreboard(self):
        self.clear()

        self.write(f"Score = {self.score}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)

