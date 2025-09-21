from vectors import Vector2i
from tile import *
from biome import BiomeTypes
from enum import IntEnum
import random

MIN_ROCK_SIZE = 2
MAX_ROCK_SIZE = 8

MIN_BUSHES_SIZE = 1
MAX_BUSHES_SIZE = 4

class FeatureTypes(IntEnum):
    ROCK = 0
    BUSHES = 1
    LENGTH = 2

class Feature:

    def __init__(self, position : Vector2i, type : float, biome : BiomeTypes, chunk_pos : Vector2i, world_seed : int):
        self.world_seed = world_seed
        self.chunk_pos = chunk_pos
        type = (type+1)/2 # Move to range [0,1]
        self.type = min(int(type*FeatureTypes.LENGTH),FeatureTypes.LENGTH - 1)
        print(type)
        print(self.type)
        self.position = position
        self.biome = biome
        self.tiles = self.make_tiles()
    
    def make_tiles(self) -> list[Tile]:
        result = []

        random.seed(self.position.x + self.position.y + self.world_seed + self.chunk_pos.x + self.chunk_pos.y)

        match (self.type):
            case (FeatureTypes.ROCK):

                for i in range(random.randint(MIN_ROCK_SIZE,MAX_ROCK_SIZE)):
                    for j in range(random.randint(MIN_ROCK_SIZE,MAX_ROCK_SIZE)):
                        pos = Vector2i(i,j) + self.position
                        tile = Stone(pos.x,pos.y,self.biome)
                        result.append(tile)
            case (FeatureTypes.BUSHES):
                for i in range(random.randint(MIN_BUSHES_SIZE,MAX_BUSHES_SIZE)):
                    for j in range(random.randint(MIN_BUSHES_SIZE,MAX_BUSHES_SIZE)):
                        if(random.choice([True, False, False])):
                            pos = Vector2i(i,j) + self.position
                            tile = Bush(pos.x,pos.y,self.biome)
                            result.append(tile)
            case(_):
                print("Faulty value, not recognized")
        
        return result

    def __str__(self):
        return f"type {self.type}, position {self.position}, tiles {self.tiles}"