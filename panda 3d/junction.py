from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3,NodePath,LoaderOptions,Texture,Loader

import random
import sys



class SmartJunction(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        super().__init__()
        loader=Loader()

        self.setup_simulation()
        model = SmartJunction.loader.loadModel("panda")
        model.reparentTo(SmartJunction.render)


    def setup_simulation(self):
        loader=Loader()

        self.accept("escape", sys.exit)
        self.colors = [(255, 0, 0), (0, 255, 0)]
        self.roadAC = loader.loadTexture("textures/roadAC.png")
        #self.roadBD = loader.loadTexture("textures/roadBD.png")
        #self.traffic_light = loader.loadTexture("textures/traffic_light.png")

        self.traffic_light_pos = Vec3(300, 300, 0)
        self.cars = []
        self.max_cars = random.randrange(0, 15)




def update(self, task):
    for c in self.cars:
        if self.traffic_light.get_pixel(0, 0) == (255, 0, 0) and c.getX() >= 250:
            c.set_x_vel(0)  # Stop updating position for cars close to the traffic light

        c.setX(c.getX() + c.getXVel())

    return task.cont


app = SmartJunction()
app.run()




class Car(NodePath):
    def __init__(self):
        NodePath.__init__(self, "car")
        self.setTexture=loader.loadTexture("textures/car.png")  # Apply the car image texture to the car geometry

        self.setPos(0, random.randrange(200, 400), 0)
        self.width = 10
        self.height = 10

        self.speed_range = (1, 4)
        self.set_x_vel(random.randint(*self.speed_range))
class Lidar:
    def __init__(self, position,range, angle):
        self.position = position

        self.range = range
        self.angle = angle