from enum import IntEnum

class BiomeTypes(IntEnum):
    FOREST = 0
    MOUNTAIN = 1
    OCEAN = 2
    LENGTH = 3


class Biome:
    def __init__(self, type : float):
        self.type : BiomeTypes = min(int(type * BiomeTypes.LENGTH),BiomeTypes.LENGTH - 1)
    
    def __str__(self):
        return f"{self.type}"