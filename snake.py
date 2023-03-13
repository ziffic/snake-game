from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            new_segment.penup()
            self.segments.append(new_segment)

    def move(self):
        for seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_num - 1].xcor()
            new_y = self.segments[seq_num - 1].ycor()
            self.segments[seq_num].goto(new_x, new_y)

    def up(self):
        self.move()
        self.segments[0].seth(90)
        self.segments[0].forward(MOVE_DISTANCE)

    def down(self):
        self.move()
        self.segments[0].setheading(270)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        self.move()
        self.segments[0].setheading(180)
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        self.move()
        self.segments[0].setheading(0)
        self.segments[0].forward(MOVE_DISTANCE)
