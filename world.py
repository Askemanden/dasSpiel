from vectors import Vector2i, Vector2f
from biome import Biome
from feature import Feature
from tile import Tile
from random import randint
from perlin_noise import PerlinNoise

class Chunk:
    def __init__(self, biome : Biome, features : list[Feature], tiles : dict[Vector2i, Tile]):
        self.biome = biome
        self.features = features
        self.tiles = tiles


class World:

    def __init__(self):
        self.seed : int = randint(0,9999)
        self.changes : list = []
        self.biomeNoise = PerlinNoise(octaves = 4, seed = self.seed)
        self.current_chunk_pos : Vector2i = Vector2i(0,0)
        chunk : Chunk = self.generate_chunk()
        self.current_biome : Biome = chunk.biome
        self.features : list[Feature] = chunk.features
        self.real_tiles : dict[Vector2i, Tile] = chunk.tiles


    
    def generate_chunk(self, direction : Vector2i) -> Chunk:
        self.current_chunk_pos += direction
        seed = int(self.seed * self.current_chunk_pos.length())
        feature_noise = PerlinNoise(octaves = 2, seed = seed)
