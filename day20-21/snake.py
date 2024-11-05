import turtle

class Snake:
    def __init__(self, starting_position):
        self.segments = []
        for position in starting_position:
            self.add_to_segments(position)
        self.old_dir = 0
        self.head = self.segments[0]
    def add_to_segments(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def update(self, old):
        self.segments.append(old)
    def restart(self, starting_position):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        for position in starting_position:
            self.add_to_segments(position)
        self.old_dir = 0
        self.head = self.segments[0]
    def move(self):
        if abs(self.head.heading() - self.old_dir) == 180:
            self.head.setheading(self.old_dir)
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].pos())
        self.segments[0].forward(20)
        self.old_dir = self.head.heading()
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def eat_itself(self):
        for i in range(1, len(self.segments)):
            if self.segments[i].distance(self.head.pos()) < 10:
                return True
        return False
            

        
