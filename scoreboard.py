from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        """Update and display the current score on the screen."""
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display the 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
            
    def increase_score(self):
        '''Increases the score by 1,clears the previous score display,and updates the scoreboard.'''
        self.score +=1
        self.clear()
        self.update_scoreboard()

        
        
