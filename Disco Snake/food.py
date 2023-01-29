from turtle import Turtle
import random

# Class for creating food for the snake to try and catch in the game
class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Setting colors, shape and size for the food and preparing the turtle module to draw the food 
        # while the turlte is invisible, not leaving lines on screen, and drawing quickly
        self.colors = ["yellow", "magenta", "green1", "cyan1", "red"]
        self.random_color = random.choice(self.colors)
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.random_color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        '''Moves one food to a new random position with a new random color.'''
        self.random_color = random.choice(self.colors)
        self.color(self.random_color)
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)