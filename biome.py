from enum import IntEnum
import pygame
from settings import *

class BiomeTypes(IntEnum):
    FOREST = 0
    MOUNTAIN = 1
    LENGTH = 2

BIOME_TEXTURES : dict[BiomeTypes, pygame.Surface] = {
    BiomeTypes.FOREST : pygame.Surface((MAP_WIDTH*TILE_SIZE,MAP_HEIGHT*TILE_SIZE)),
    BiomeTypes.MOUNTAIN : pygame.Surface((MAP_WIDTH*TILE_SIZE,MAP_HEIGHT*TILE_SIZE))
}

DEFAULT_TEXTURE : pygame.Surface = pygame.Surface((MAP_WIDTH*TILE_SIZE,MAP_HEIGHT*TILE_SIZE))

DEFAULT_TEXTURE.fill((50,50,50))
BIOME_TEXTURES.get(BiomeTypes.FOREST).fill((0,230,20))
BIOME_TEXTURES.get(BiomeTypes.MOUNTAIN).fill((255,20,30))


class Biome:
    def __init__(self, type : float):
        type = (type+1)/2 # [-1,1] -> [0,1]
        self.type : BiomeTypes = min(int(type * BiomeTypes.LENGTH),BiomeTypes.LENGTH - 1)
        self.texture : pygame.Surface = BIOME_TEXTURES.get(self.type, DEFAULT_TEXTURE)
    
    def __str__(self):
        return f"{self.type}"
    
    def draw(self, surface : pygame.Surface):
        surface.blit(self.texture,(0,0))