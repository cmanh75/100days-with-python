import random
from turtle import Turtle

COLORS = ["red", "yellow", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5;
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        number = random.randint(1, 6)
        if number != 5:
            return 
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)
    def move_all(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                self.all_cars.remove(car)
                continue
            car.forward(self.speed)
    def level_up(self):
        for car in self.all_cars:
            car.hideturtle()
        self.speed += MOVE_INCREMENT
        self.all_cars.clear()