from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        #self.shape("square")
        self.penup()
        self.setheading(180)
        self.goto(x=300, y=random.randint(-260, 260))
        self.car = []

    def generate_cars(self):
        for color_index in COLORS:
            new_car = Turtle(shape="square")
            new_car.goto(x=300, y=random.randint(-260, 260))
            new_car.color(color_index)


    def movement(self):
        self.forward(STARTING_MOVE_DISTANCE)
