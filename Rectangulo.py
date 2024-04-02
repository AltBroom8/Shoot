import pyglet
from pyglet import shapes
class Rectangulo(pyglet.shapes.Rectangle):

    def __init__(self, *args, **kwargs):
        super(Rectangulo, self).__init__(*args, **kwargs)
