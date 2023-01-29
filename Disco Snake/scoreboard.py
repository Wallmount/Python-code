from turtle import Turtle

# Class for creating scoreboard that shows current score and high score
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # Setting text color, position and hiding turtle. Reading the 
        # high score data file and updating the score board.
        self.goto(0,270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt") as data_file:
            self.highscore = int(data_file.read())
        self.update()


    def new_game(self):
        '''Saves the current score into a file if it is higher than current hight score.'''
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(f"{self.highscore}")
        self.score = 0
        self.update()


    def update(self):
        '''Clears and updates the scoreboard.'''
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", 
        align="center", font=("Comic Sans", 15, "normal"))


    def add_point(self):
        '''Adds a point to the current score.'''
        self.score += 1
        self.update()

