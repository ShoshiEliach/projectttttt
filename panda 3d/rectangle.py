from panda3d.core import Geom, GeomVertexFormat, GeomVertexData, GeomVertexWriter
from panda3d.core import GeomTriangles, GeomNode, GeomVertexFormat, GeomVertexData, GeomVertexFormat,Material
from panda3d.core import NodePath, AmbientLight

from direct.showbase.ShowBase import ShowBase


def create_rectangle(x1, y1, x2, y2, render):
    format = GeomVertexFormat.getV3()
    vdata = GeomVertexData('rectangle', format, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, 'vertex')

    vertex.addData3f(x1, 0, y1)
    vertex.addData3f(x2, 0, y1)
    vertex.addData3f(x2, 0, y2)
    vertex.addData3f(x1, 0, y2)

    tris = GeomTriangles(Geom.UHStatic)
    tris.addVertices(0, 1, 2)
    tris.closePrimitive()
    tris.addVertices(2, 3, 0)
    tris.closePrimitive()

    geom = Geom(vdata)
    geom.addPrimitive(tris)

    node = GeomNode('rectangle')
    node.addGeom(geom)
    material = Material()
    material.setDiffuse((1, 0, 0, 1))  # Set the diffuse color of the material to red
    material.setShininess(10)  # Set the shininess of the material

    rectangle = NodePath(node)
    rectangle.setMaterial(Material())
    rectangle.setColor((1, 0, 0, 1))
    rectangle.reparentTo(render)

    # Create an ambient light
    ambient_light = AmbientLight('ambient_light')
    ambient_light.setColor((1, 1, 1, 1))
    ambient_light_nodepath = render.attachNewNode(ambient_light)

    # Attach the ambient light to the render
    render.setLight(ambient_light_nodepath)


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #self.camera.setPos(x, y, z)  # Set the position of the camera
        self.camera.lookAt(0, 0, 0)
        self.camLens.setFov(60)  # Set the field of view of the camera to 60 degrees
        self.camLens.setAspectRatio(1.33)
        create_rectangle(-1, -1, 1, 1,self.render)

app = MyApp()
app.run()