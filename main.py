from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Satvik's Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")





food = Food()
score = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collisions with Food(snake.turtle_obj[0] is the snake's head)
    if snake.turtle_obj[0].distance(food) < 15:
        food.refresh_food()
        snake.add_snake_body()
        score.score_update()

    # Detecting Collisions with wall
    if snake.turtle_obj[0].xcor() > 300 or snake.turtle_obj[0].xcor() < -300 or snake.turtle_obj[0].ycor() > 300 or snake.turtle_obj[0].ycor() < -300:
        score.reset_score_board()
        snake.reset_snake()


    # Detecting Collision with Tail
    for tim in snake.turtle_obj:
        if tim == snake.turtle_obj[0]:
            continue
        elif snake.turtle_obj[0].distance(tim) < 10:
            snake.reset_snake()
            score.reset_score_board()


















screen.exitonclick()
