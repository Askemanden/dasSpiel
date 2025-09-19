from vectors import Vector2i
from tile import Tile
from pathfind import Pathfinder
import pygame

MAP_WIDTH = 10
MAP_HEIGHT = 10

#Dummy texture (pygame.Surface required by Tile)
pygame.init()
dummy_texture = pygame.Surface((1, 1))

def make_test_map():
    tiles = {}
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            tiles[Vector2i(x, y)] = Tile(x, y, True, dummy_texture)

    # vertical wall at x=3, except at y=4 (gap)
    for y in range(MAP_HEIGHT):
        if y != 4:  # leave a gap
            tiles[Vector2i(3, y)] = Tile(3, y, False, dummy_texture)

    # horizontal wall at y=6, from x=5..9
    for x in range(5, MAP_WIDTH):
        tiles[Vector2i(x, 6)] = Tile(x, 6, False, dummy_texture)

    return tiles

if __name__ == "__main__":
    tiles = make_test_map()
    pf = Pathfinder(tiles)

    start = Vector2i(0, 0)
    goal = Vector2i(9, 9)

    path = pf.find_path(start, goal)

    if path is None:
        print("No path found")
    else:
        print("Path length:", len(path))
        print("Path:", [(p.x, p.y) for p in path])
