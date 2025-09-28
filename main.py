from signals import *
from world import *
from Player import *
from pathfind import *
from tile import Tile
import pygame


def main():

    # PYGAME SETUP
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE, MAP_HEIGHT*TILE_SIZE))
    pygame.display.set_caption("World Draw Test")

    # SIGNALS
    leftClick : Signal = Signal()


    world = World()
    real_tiles : list[Tile] = world.real_tiles.values()
    blocked = []
    for tile in real_tiles:
        if not tile.passable:
            blocked.append(tile.position)
    player = Player(10)
    player.path = astar(player.grid_position,Vector2i(1,0),blocked)

    running = True
    clock = pygame.time.Clock()
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)

        screen.fill((0, 0, 0))  # Clear screen
        world.draw(screen)      # Draw the world
        player.draw(screen)
        pygame.display.flip()   # Update display
        dt = clock.tick(60)          # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()