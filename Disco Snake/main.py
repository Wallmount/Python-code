# A snake game built with the turtle module.

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SLEEP_TIME = 0.15

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

def reset_sleep_time():
    '''Resets sleep time to starting value.'''
    global SLEEP_TIME
    SLEEP_TIME = 0.15

def decrease_sleep_time():
    '''Decreases sleep time, resulting in higher snake speed.'''
    global SLEEP_TIME
    SLEEP_TIME -= 0.01

# Initializing snake, food and scoreboard and enabling controlling of the snake
snake = Snake()
foods = []
scoreboard = Scoreboard()

for _ in range(8):
    food = Food()
    foods.append(food)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Game loop
game_is_on = True

while game_is_on:
    # Moving snake
    screen.update()
    time.sleep(SLEEP_TIME)

    snake.move()
    snake.glitter()

    #Detecting snake-food collision, increasing score, snake length and speed
    for food in foods:
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_point()
            snake.add_segment()
            decrease_sleep_time()

    #Detecting snake-wall collision, restarting game and resetting snake speed
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.new_game()
        snake.new_game()
        reset_sleep_time()
        

    #Detecting snake head- snake body collision, restarting game and resetting snake speed
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.new_game()
            snake.new_game()
            reset_sleep_time()

screen.exitonclick()