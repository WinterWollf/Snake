from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

GAME_STATUS = True

# Screen setup
screen = Screen()
screen.listen()
screen.tracer(n=0)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")

# Game setup
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="W", fun=snake.up)
screen.onkey(key="S", fun=snake.down)
screen.onkey(key="D", fun=snake.right)
screen.onkey(key="A", fun=snake.left)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


while GAME_STATUS:
    screen.update()
    time.sleep(0.1)

    snake.move()
    snake.food_colision_detection(food, scoreboard)
    if snake.wall_colision_detection() == False or snake.tail_colision_detection() == False:
        GAME_STATUS = False

scoreboard.game_over()
screen.exitonclick()
