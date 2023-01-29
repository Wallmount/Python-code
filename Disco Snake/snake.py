from turtle import Turtle
import time
import random

# Class for creating the snake
class Snake:

    def __init__(self):
        # Creating lists for the snakes segments, colors and defining the snakes head
        self.segments = []
        self.colors = ["white", "hotpink", "DeepSkyBlue2", "GreenYellow", "pink", "magenta", "plum1", "white",
                       "PaleGreen1", "SlateBlue1", "yellow", "green1", ]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''Creates the snake at the center of the screen, made from 3 square shaped segments 
        and random colors. Makes sure the snake doeas not leave lines on the screen.'''
        x = 20
        for _ in range(3):    
            random_color = random.choice(self.colors)
            turtle = Turtle()
            turtle.shape("square")
            turtle.color(random_color)
            turtle.penup()
            x -= 20
            turtle.goto(x, 0)
            self.segments.append(turtle)

    def add_segment(self):
        '''Adds a segment to the snakes body, making it longer.'''
        random_color = random.choice(self.colors)
        turtle = Turtle()
        turtle.shape("square")
        turtle.color(random_color)
        turtle.penup()
        turtle.goto(self.segments[-1].position())
        self.segments.append(turtle)

    def glitter(self):
        '''Makes the whole snake glitter in rainbow colors.'''
        for seg_num in range(len(self.segments)):
            new_color = random.choice(self.colors)
            self.segments[seg_num].color(new_color)

    def move(self):
        '''Makes the snake move forward by moving the head forward and 
        making the segments follow after the segment before.'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)


    def new_game(self):
        '''Recreates the snake to the length of 3 segments and moves it back 
        to the starting position (middle of the screen).'''
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        '''Turns the snake upwards'''
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        '''Turns the snake left'''
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        '''Turns the snake right.'''
        if self.head.heading() != 180:
            self.segments[0].setheading(0)

    def down(self):
        '''Turns the snake downwards.'''
        if self.head.heading() != 90:
            self.segments[0].setheading(270)