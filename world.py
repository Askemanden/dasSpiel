from vectors import Vector2i, Vector2f
from biome import Biome
from feature import Feature
from tile import Tile
from random import randint

class World:

    def __init__(self):
        self.seed : int = randint(0,9999)
        self.current_chunk_pos : Vector2i = Vector2i(0,0)
        chunk = self.generate_chunk()
        self.current_biome : Biome = chunk["Biome"]
        self.features : list[Feature] = chunk["Features"]
        self.real_tiles : dict[Vector2i, Tile] = chunk["Tiles"]
    
    def generate_chunk(self) -> dict:
        pass

        