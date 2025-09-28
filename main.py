from signals import *
from world import *
from Player import *
from pathfind import *
from tile import Tile
import pygame
from random import randint


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
    player = Player(health=10, speed = 0.15)
    player.set_path(astar(player.grid_position,Vector2i(0,0),blocked),Vector2f(20,10))
    running = True
    clock = pygame.time.Clock()
    dt = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(dt)

    screen.fill((0, 0, 0))  # Clear screen
    world.draw(screen)      # Draw the world
    player.draw(screen)
    pygame.display.flip()   # Update display
    dt = clock.tick(1)          # Limit to 60 FPS

    i = 0

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
        i+=1
        if(i==50):
            i = 0
            player.set_path(astar(player.grid_position,Vector2i(randint(0,MAP_WIDTH),randint(0,MAP_HEIGHT)),blocked),Vector2f(randint(0,TILE_SIZE),randint(0,TILE_SIZE)))


    pygame.quit()

if __name__ == "__main__":
    main()