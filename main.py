from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
score.show_scoreboard()

snake.control_direction()

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    # detect collision with food
    for i in snake.objects:
        if i.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

    # detect collision with wall
    for i in snake.objects:
        if i.xcor() > 280 or i.xcor() < -280 or i.ycor() > 280 or i.ycor() < -280:
            score.high_score()
            snake.reset()
           # game_on = False
           # score.game_over()

    # detect collision with tail
    for i in snake.objects[1:]:
        if snake.objects[0].distance(i) < 10:
            score.high_score()
            snake.reset()
          #  game_on = False
            #score.game_over()

screen.exitonclick()
