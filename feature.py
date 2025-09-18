from vectors import Vector2i
from tile import *
from biome import BiomeTypes
from enum import Enum

class FeatureTypes(Enum):
    LARGE_ROCK = 0
    SMALL_ROCK = 1
    BUSH = 2
    LENGTH = 3


class Feature:

    def __init__(self, position : Vector2i, type : float, biome : BiomeTypes):
        self.type = int(type*FeatureTypes.LENGTH)
        self.position = position
        self.tiles = self.make_tiles()
    
    def make_tiles(self) -> list[Tile]:
        pass