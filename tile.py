from vectors import Vector2i
from signals import Signal
import pygame
from settings import *
from biome import BiomeTypes
import numpy as np


BIOME_COLOR_MODULATIONS = {
    BiomeTypes.FOREST : (20,240,30,50),
    BiomeTypes.MOUNTAIN : (255, 0, 30,50)
}

# TODO : LAV PYGAME INITIALIZER SÅ DISSE LINJER IKKE BEHØVES
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

STONE_TEXTURE = pygame.transform.scale(pygame.image.load("resources/textures/stone.png").convert_alpha(), (TILE_SIZE,TILE_SIZE))
WOOD_TEXTURE = pygame.transform.scale(pygame.image.load("resources/textures/wood.png").convert_alpha(), (TILE_SIZE,TILE_SIZE))
BUSH_TEXTURE = pygame.transform.scale(pygame.image.load("resources/textures/bush.png").convert_alpha(), (TILE_SIZE,TILE_SIZE))

def modulate_texture(base_texture: pygame.Surface, biome: BiomeTypes) -> pygame.Surface:
    tint = BIOME_COLOR_MODULATIONS.get(biome, (255, 255, 255, 0))  # RGBA
    texture = base_texture.copy()

    # Extract pixel arrays
    rgb_array = pygame.surfarray.pixels3d(texture)
    alpha_array = pygame.surfarray.pixels_alpha(texture)

    # Normalize tint strength from alpha channel (0–255 → 0.0–1.0)
    strength = tint[3] / 255.0
    tint_rgb = np.array(tint[:3], dtype=np.float32)

    # Blend only visible pixels
    for x in range(texture.get_width()):
        for y in range(texture.get_height()):
            if alpha_array[x, y] > 0:
                original = rgb_array[x, y].astype(np.float32)
                blended = original * (1 - strength) + tint_rgb * strength
                rgb_array[x, y] = blended.astype(np.uint8)

    return texture


class Tile:
    def __init__(self, x : int, y : int, passable : bool, texture : pygame.Surface):
        self.position : Vector2i = Vector2i(x,y)
        self.passable : bool = passable
        self.texture : pygame.Surface = texture
        self.on_interact : Signal = Signal()
    
    def __str__(self):
        return f"pos {self.position}, passable {self.passable}"
    
    def draw(self, surface : pygame.Surface):
        surface.blit(self.texture,(self.position.x*TILE_SIZE, self.position.y*TILE_SIZE))

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

