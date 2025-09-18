from vectors import Vector2i, Vector2f
from biome import Biome
from feature import Feature
from tile import Tile
from random import randint
from perlin_noise import PerlinNoise
from settings import *

class Chunk:
    def __init__(self, biome : Biome, features : list[Feature], tiles : dict[Vector2i, Tile]):
        self.biome = biome
        self.features = features
        self.tiles = tiles
    
    def __str__(self):
        return f"biome : {self.biome}, features : {self.features}, tiles {self.tiles}"


class World:
    def __init__(self):
        self.seed : int = randint(0,9999)
        self.changes : list = []
        self.biomeNoise = PerlinNoise(octaves = 4, seed = self.seed)
        self.current_chunk_pos : Vector2i = Vector2i(0,0)

        self.chunk : Chunk = self.generate_chunk()
        self.current_biome : Biome = self.chunk.biome
        self.features : list[Feature] = self.chunk.features
        self.real_tiles : dict[Vector2i, Tile] = self.chunk.tiles


    def generate_chunk(self) -> Chunk:
        seed = int(self.seed * self.current_chunk_pos.length())
        feature_noise = PerlinNoise(octaves = 2, seed = seed)
        biome = Biome(self.biomeNoise([self.current_chunk_pos.x,self.current_chunk_pos.y]))
        features : list[Feature]= []
        for i in range(0, MAP_WIDTH, FEATURE_FREQUENCY):
            for j in range(0, MAP_HEIGHT, FEATURE_FREQUENCY):
                noise_val = feature_noise([i / MAP_WIDTH, j / MAP_HEIGHT])
                features.append(Feature(Vector2i(i, j), noise_val,biome.type))
        tiles_list : list[Tile] = []

        for feature in features:
            tiles_list.extend(feature.tiles)
        
        tiles : dict[Vector2i, Tile] = {}

        for tile in tiles_list:
            tiles[tile.position] = tile
        
        return Chunk(biome, features, tiles)


        
if __name__ == "__main__":
    print(Vector2i(0,0).x, Vector2i(0,0).y)
    world = World()
    print(world.seed, " ", world.changes, " ", world.biomeNoise, " ", world.current_chunk_pos, " ", world.chunk)