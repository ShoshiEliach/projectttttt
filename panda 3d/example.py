from direct.showbase.ShowBase import ShowBase
from panda3d.core import Geom, GeomVertexFormat, GeomVertexData, GeomVertexWriter, GeomTriangles, Geom, GeomNode,GeomLines,Loader
from panda3d.core import Vec3, VBase4
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import loadPrcFileData, NodePath, WindowProperties



class RoadIntersectionSimulation(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        cube_model = self.loader.loadModel("models/cube_car.egg")
        cube_model.reparentTo(self.render)
        cube_model.setPos(-10, 0, 0)
        # Create roads
        road1_points = [(-10, 0, 0), (10, 0, 0)]
        road2_points = [(0, -10, 0), (0, 10, 0)]

        road1 = self.create_road(road1_points)
        road2 = self.create_road(road2_points)

        # Create cars
        car1 = self.create_car((-10, 0, 0), (1, 0, 0))
        car2 = self.create_car((10, 0, 0), (-1, 0, 0))
        car3 = self.create_car((0, -10, 0), (0, 1, 0))
        car4 = self.create_car((0, 10, 0), (0, -1, 0))

    def create_road(self, points):
        format = GeomVertexFormat.getV3n3()
        vdata = GeomVertexData('road_data', format, Geom.UHStatic)
        vertex_writer = GeomVertexWriter(vdata, 'vertex')

        for point in points:
            vertex_writer.addData3f(point[0], point[1], point[2])

        prim = GeomLines(Geom.UHStatic)
        prim.addVertices(0, 1)

        geom = Geom(vdata)
        geom.addPrimitive(prim)

        node = GeomNode('road')
        node.addGeom(geom)

        road = self.render.attachNewNode(node)
        return road

    def create_car(self, pos, direction):
        def create_car(self, pos, direction):
            #car_model = loader.loadModel("models/car")  # Update this line with the correct path to the model file
            car_model.reparentTo(self.render)
app = RoadIntersectionSimulation()
app.run()