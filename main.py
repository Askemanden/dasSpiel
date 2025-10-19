from signals import *
from world import *
from Player import *
from pathfind import *
from tile import Tile
import pygame
from WindowPartitioner import *

LEFT = 1
RIGHT = 3

main_menu = True
running = True

def quit():
    print("Game Quit")
    global running
    running = False
    global main_menu
    main_menu = False


def start():
    print("Game Started")
    global main_menu
    main_menu = False
    global running
    running = True

function_map = {
    "quit": quit,
    "start": start,
    None: None
}

def esc_menu(menu, screen):
        menu.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            else:
                menu.event_handler(event)
        menu.draw(screen)
        pygame.display.flip()


def main():

    # PYGAME SETUP
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE, MAP_HEIGHT*TILE_SIZE))
    pygame.display.set_caption("Das Spiel die Übermenschen")

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

    global running
    global main_menu
    clock = pygame.time.Clock()
    dt = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()

    player.update(dt)

    screen.fill((0, 0, 0))  # Clear screen
    world.draw(screen)      # Draw the world
    player.draw(screen)
    with open("menu.json", "r", encoding="utf-8") as f:
        menu_data = json.load(f)
    quit_menu = create_menu_from_json(menu_data, 0, function_map)
    paused_text = create_menu_from_json(menu_data, 1, function_map)
    pygame.display.flip()   # Update display
    #dt = clock.tick(1)          # Limit to 60 FPS

    while running:
        if main_menu:
            world.draw(screen)
            player.draw(screen)
            paused_text.draw(screen)
            esc_menu(quit_menu, screen)
            
            continue

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu = True


        player.update(dt)

        screen.fill((0, 0, 0))  # Clear screen
        world.draw(screen)      # Draw the world
        player.draw(screen)
        pygame.display.flip()   # Update display
        dt = clock.tick(60)     # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()