from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
# turtle.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Colliosion with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.addscore()

    # Detect Colliosion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        # time.sleep(10)
        snake.reset()
        score.reset()

    # Detect Self Collision
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset()
            score.reset()


screen.exitonclick()
