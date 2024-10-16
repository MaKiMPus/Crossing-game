from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance = random.randint(1, 5) #random chance to create new car
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)
    
    def move_cars(self):
        for car in self.all_car:
            car.backward(self.car_speed)
    
    def recreate_cars(self):
        self.create_car()
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    
    
        
    