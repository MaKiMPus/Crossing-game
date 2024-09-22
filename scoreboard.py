from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"
LOCATION = (-230,270)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(LOCATION)
        self.write(f"Score = {self.score}", font=FONT, align=ALIGNMENT)
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over!, Your score is {self.score}", font=FONT, align=ALIGNMENT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
        