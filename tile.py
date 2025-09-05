from vectors import Vector2i

class Tile:

    def __init__(self, x, y, passable, texture):
        self.position = Vector2i(x,y)
        self.passable = passable
        self.texture = texture