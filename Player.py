from entityetellerandetcomposites import*
from settings import*
import pygame

class palyer:
    def __init__(self, world_x = 0, world_y = 0):
        self.world_x = world_x
        self.world_y = world_y
        self.health = 100
        self.attack_power = 5   # Damage per attack-turn
        self.speed = 5  # Tiles per move-turn

    def draw(self, screen):
        pygame.draw.circle(screen, (40, 200, 100), self.world_x, self.world_y, 15)