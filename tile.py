from vectors import Vector2i
from signals import Signal
import pygame
from settings import *
from biome import BiomeTypes

BIOME_COLOR_MODULATIONS = {
    BiomeTypes.FOREST : (20,240,30),
    BiomeTypes.MOUNTAIN : (255, 0, 30)
}

STONE_TEXTURE = pygame.transform.scale(pygame.image.load("resources/textures/stone.png").convert_alpha(), (TILE_SIZE,TILE_SIZE))
WOOD_TEXTURE = pygame.transform.scale(pygame.image.load("resources/textures/wood.png").convert_alpha(), (TILE_SIZE,TILE_SIZE))
BUSH_TEXTURE = pygame.transform.scale(pygame.image.load("resources/textures/bush.png").convert_alpha(), (TILE_SIZE,TILE_SIZE))

def modulate_texture(base_texture : pygame.Surface, biome : BiomeTypes):
    tint = BIOME_COLOR_MODULATIONS.get(biome, (255, 255, 255))
    texture = base_texture.copy()
    texture.fill(tint, special_flags=pygame.BLEND_RGBA_MULT)
    return texture

class Tile:
    def __init__(self, x : int, y : int, passable : bool, texture : pygame.Surface):
        self.position : Vector2i = Vector2i(x,y)
        self.passable : bool = passable
        self.texture : pygame.Surface = texture
        self.on_interact : Signal = Signal()
    
    def __str__(self):
        return f"pos {self.position}, passable {self.passable}"

class Stone(Tile):
    def __init__(self, x, y, biome : BiomeTypes):
        texture = modulate_texture(STONE_TEXTURE, biome)
        super().__init__(x,y,False,texture)

class Wood(Tile):
    def __init__(self, x, y, biome : BiomeTypes):
        texture = modulate_texture(WOOD_TEXTURE, biome)
        super().__init__(x,y,False,texture)

class Bush(Tile):
    def __init__(self, x, y, biome : BiomeTypes):
        texture = modulate_texture(BUSH_TEXTURE, biome)
        super().__init__(x,y,True,texture)

