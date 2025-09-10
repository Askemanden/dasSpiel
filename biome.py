from enum import Enum

class BiomeTypes(Enum):
    FOREST = 0
    MOUNTAIN = 1
    OCEAN = 2

class Biome:
    def __init__(self, type : int):
        self.type = type