from turtle import Turtle, Screen

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SCREEN = Screen()


class Snake:

    def __init__(self):
        self.objects = []
        self.create_snake()

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(pos)
        self.objects.append(snake)

    def extend(self):
        self.add_segment(self.objects[-1].position())

    def move(self):
        for obj in range(len(self.objects) - 1, 0, -1):
            new_x = self.objects[obj - 1].xcor()
            new_y = self.objects[obj - 1].ycor()
            self.objects[obj].goto(new_x, new_y)
        self.objects[0].forward(MOVE_DISTANCE)

    def up(self):
        for i in self.objects:
            if i.heading() != 270:
                i.seth(90)

    def down(self):
        for i in self.objects:
            if i.heading() != 90:
                i.seth(270)

    def left(self):
        for i in self.objects:
            if i.heading() != 0:
                i.seth(180)

    def right(self):
        for i in self.objects:
            if i.heading() != 180:
                i.seth(0)

    def control_direction(self):
        SCREEN.listen()
        SCREEN.onkey(self.up, "Up")
        SCREEN.onkey(self.down, "Down")
        SCREEN.onkey(self.left, "Left")
        SCREEN.onkey(self.right, "Right")

    def reset(self):
        for obj in self.objects:
            obj.goto(1000,1000)
        self.objects.clear()
        self.create_snake()
