from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.turtle_obj = []
        self.snake_body()

    def snake_body(self):
        for postion in POSITIONS:
            tim = Turtle("square")
            tim.color("deeppink3")
            tim.penup()
            tim.goto(postion)
            self.turtle_obj.append(tim)

    def add_snake_body(self):
        new_tim = Turtle("square")
        new_tim.color("deeppink3")
        new_tim.penup()
        new_tim.goto(self.turtle_obj[-1].position())    #refering to last tim object
        self.turtle_obj.append(new_tim)

    def reset_snake(self):
        for snake_seg in self.turtle_obj:
            snake_seg.goto(1000, 1000)
        self.turtle_obj.clear()
        self.snake_body()

    def move(self):
        for i in range(len(self.turtle_obj) - 1, 0, -1):
            new_x = self.turtle_obj[i - 1].xcor()
            new_y = self.turtle_obj[i - 1].ycor()
            self.turtle_obj[i].goto(new_x, new_y)
        self.turtle_obj[0].forward(20)

# Screen methods
    def up(self):
        if self.turtle_obj[0].heading() != (270):
            self.turtle_obj[0].setheading(90)

    def down(self):
        if self.turtle_obj[0].heading() != 90:
            self.turtle_obj[0].setheading(270)

    def left(self):
        if self.turtle_obj[0].heading() != 0:
            self.turtle_obj[0].setheading(180)

    def right(self):
        if self.turtle_obj[0].heading() != 180:
            self.turtle_obj[0].setheading(0)




