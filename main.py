from signals import *
from world import *
from Player import *
from pathfind import *
from tile import Tile
import pygame

LEFT = 1
RIGHT = 3

def main():

    # PYGAME SETUP
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE, MAP_HEIGHT*TILE_SIZE))
    pygame.display.set_caption("World Draw Test")

    world = World()
    player = Player(health=10)

    # SIGNALS
    leftClick : Signal = Signal()
    rightClick : Signal = Signal()

    # CONNECT SIGNALS IN ORDER OF CONSUMPTION (CONNECTIONS THAT SHOULD CONSUME SHOULD BE PLACED FIRST)

    # LEFT CLICK CONNECTIONS
    leftClick.connect("move player", player.newTarget)

    # RIGHT CLICK CONNECTIONS
    rightClick.connect("interact", player.interact)

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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    leftClick.emit([event.pos, world])
                    print("l")
                elif event.button == RIGHT:
                    print("r")
                    rightClick.emit([event.pos, world])


        player.update(dt)

        screen.fill((0, 0, 0))  # Clear screen
        world.draw(screen)      # Draw the world
        player.draw(screen)
        pygame.display.flip()   # Update display
        dt = clock.tick(60)     # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()