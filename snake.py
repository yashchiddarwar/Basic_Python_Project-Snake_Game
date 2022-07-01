import time
from turtle import *
from scoreboard import Scoreboard
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.extend(positions)

    def extend(self, positions):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(positions)
        self.turtle_list.append(new_turtle)

    def add_head(self):
        self.extend(self.turtle_list[-1].position())








        # x = 0
        # for _ in range(3):
        #     new_turtle = Turtle()
        #     self.turtle_list.append(new_turtle)
        #
        # for turtle in self.turtle_list:
        #     turtle.shape("square")
        #     turtle.color("white")
        #     turtle.penup()
        #     turtle.goto(x, 0)
        #     x = x - 20

    def move(self):
        for turtle_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle_num - 1].xcor()
            new_y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

