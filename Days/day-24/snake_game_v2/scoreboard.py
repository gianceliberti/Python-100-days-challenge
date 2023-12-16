from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    """create a score at the top of the program"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/home/gianceli/Desktop/Python-100-days/Days/day-24/snake_game_v2/data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}",align= ALIGNMENT,font = FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/home/gianceli/Desktop/Python-100-days/Days/day-24/snake_game_v2/data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

              
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
    