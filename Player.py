from entityetellerandetcomposites import*
from settings import*
from vectors import*
import pygame

class player:
    def __init__(self, world_x = 0, world_y = 0):
        self.position = Vector2f(world_x,world_y)
        self.grid_position = Vector2i(0, 0)
        self.health = 100
        self.attack_power = 5                       # Damage per attack-turn
        self.speed = 5                              # Tiles per move-turn

    def draw(self, screen):
        pygame.draw.circle(screen, (40, 200, 100), self.world_x, self.world_y, 15)