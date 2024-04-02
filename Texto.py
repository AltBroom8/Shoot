import pyglet
class Texto(pyglet.text.Label):
    def __init__(self, *args, **kwargs):
        super(Texto, self).__init__(*args, **kwargs)