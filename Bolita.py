import pyglet

class Bolita(pyglet.shapes.Circle):

    def __init__(self, *args, **kwargs):
        super(Bolita, self).__init__(*args, **kwargs)