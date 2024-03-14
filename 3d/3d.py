from vpython import *
import random
import pybullet


# Set rate (frames per second)
rate_value = 60

# Set colors
road_color = color.yellow
traffic_light_color = color.red
car_color = color.red

scene = canvas()
#mygroup = group(pos=vec(1,-1,3) )



max_cars = random.randrange(0, 15)
cars = []

class CarA:
    def __init__(self):
        self.car = box(pos=vec(0,0,0), size=vector(20, 20, 20), color=car_color)
        self.speed_range = (1, 4)
        self.vel=1
        #self.vel = random.uniform(*self.speed_range)
        #self.velY=
        #self.velZ
roadA = box(pos=vec(0, 0, 0), length=1700, height=250, width=550, color=color.cyan)
roadBD= box(pos=vec(5, 10, 7), length=250, height=1000, width=550, color=color.yellow)
#AtoC = shapes.rectangle(width=10, height=6,pos=vec(0,0,0))

traffic_lightC = box(pos=vector(0, 50, 300), size=vector(5, 60, 81), color=traffic_light_color)

lidarC = box(pos=vector(250, 200, 0), size=vector(1, 200, 200), color=color.white)


while True:
    rate(rate_value)
    if random.random() < 0.01:
       cars.append(CarA())

    for c in cars:
        if traffic_lightC.color == color.red and c.car.pos.x >= 300:
            c.vel = 0  # Stop updating position for cars close to the traffic light

        c.car.pos.x += c.vel
