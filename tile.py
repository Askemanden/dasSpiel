from vectors import Vector2i
from signals import Signal
import pygame
from settings import *
from biome import BiomeTypes

class Tile:
    def __init__(self, x : int, y : int, passable : bool, texture : pygame.Surface):
        self.position : Vector2i = Vector2i(x,y)
        self.passable : bool = passable
        self.texture : pygame.Surface = texture
        pygame.transform.scale(self.texture, (TILE_SIZE,TILE_SIZE))
        self.on_interact : Signal = Signal()
    
    def __str__(self):
        return f"pos {self.position}, passable {self.passable}"

class Stone(Tile):
    def __init__(self, x, y, biome : int):
        if(biome == BiomeTypes.FOREST):
            texture = pygame.image.load("resources/textures/stone.png").convert_alpha()
        super.__init__(x,y,False,texture)

class Wood(Tile):
    def __init__(self, x, y, biome : int):
        if(biome == BiomeTypes.FOREST):
            texture = pygame.image.load("resources/textures/wood.png").convert_alpha()
        super.__init__(x,y,False,texture)

class Bush(Tile):
    def __init__(self, x, y, biome : int):
        if(biome == BiomeTypes.FOREST):
            texture = pygame.image.load("resources/textures/bush.png").convert_alpha()
        super.__init__(x,y,True,texture)

