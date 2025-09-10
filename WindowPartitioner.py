import pygame
from vectors import Vector2f
import enum

class screen_box:
    def __init__(self, x, y, width, height):
        self.screen_position = Vector2f(x - width * 0.5, y - height * 0.5)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (230,5,5), self.rect)

def ikke_en_skid():
    pass


class container_type(enum.Enum):
    item = 0
    button = 1

class container:
    def __init__(self, type, function = ikke_en_skid):
        self.on_click = function
        self.container_type = type


if __name__ == ("__main__"):
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Window Partitioner")
    running = True
    screen_box = screen_box(50, 50, 200, 200)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen_box.draw(screen)
        pygame.display.flip()