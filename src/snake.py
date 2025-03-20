from turtle import Turtle

MOVE_DISTANCE = 12
BORDER = 290


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            part = Turtle(shape="square")
            part.penup()
            part.color("white")
            part.goto(x=-MOVE_DISTANCE * i, y=0)
            self.segments.append(part)

    def move(self):
        previous_position = self.head.position()
        self.head.forward(MOVE_DISTANCE)
        for a in range(1, len(self.segments)):
            previous_position2 = self.segments[a].position()
            self.segments[a].goto(previous_position)
            previous_position = previous_position2


    def grow(self):
        part = Turtle(shape="square")
        part.penup()
        part.color("gray")
        part.goto(x=self.segments[-1].xcor(), y=self.segments[-1].ycor())
        self.segments.append(part)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def food_colision_detection(self, food, scoreboard):
        if self.head.distance(food) < 15:
            food.relocate()
            scoreboard.update_score()
            self.grow()
            return True
        else:
            return False

    def wall_colision_detection(self):
        if self.head.xcor() >= BORDER or self.head.xcor() <= -BORDER or self.head.ycor() >= BORDER or self.head.ycor() <= -BORDER:
            return False

    def tail_colision_detection(self):
        for i in range(1, len(self.segments)):
            if self.head.distance(self.segments[i]) < 10:
                return False
