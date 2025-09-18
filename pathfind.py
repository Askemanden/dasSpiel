'''
Pathfinding modul ved brug af A* algoritmen.
'''
from heapq import heappush, heappop
from vectors import Vector2i
from tile import Tile
from settings import *

class Pathfinder:
    #Pathfinding baseret på A* algoritmen
    def __init__(self, real_tiles:dict[Vector2i,Tile]):

        self.real_tiles : dict[Vector2i,Tile] = real_tiles

        self.directions = [
            (0, 1, 70), (0, -1, 70), (1, 0, 70), (-1, 0, 70),
            (1, 1, 99), (-1, 1, 99), (1, -1, 99), (-1, -1, 99)
        ]

    def is_passable(self, x, y):
        tile = self.real_tiles.get(Vector2i(x, y))
        return tile is not None and tile.passable

    def in_bounds(self, x, y):
        return 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT

    def heuristic(self, a: Vector2i, b: Vector2i) -> int:
        D=70
        D2=99
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def find_path(self, start: Vector2i, goal: Vector2i):
        if not self.in_bounds(start.x, start.y) or not self.in_bounds(goal.x, goal.y):
            return None # start eller mål er uden for grænserne
        if not self.is_passable(start.x, start.y) or not self.is_passable(goal.x, goal.y):
            return None # start eller mål er ikke passable
        
        open_heap = []
        heappush(open_heap, (0, start))
        came_from = {}
        g_score = { (start.x, start.y): 0 }

        while open_heap:
            _, current = heappop(open_heap)

            if (current.x, current.y) == (goal.x, goal.y):
                return self.reconstruct_path(came_from, current)

            for dx, dy, cost in self.directions:
                nx, ny = current.x + dx, current.y + dy
                if not self.in_bounds(nx, ny):
                    continue
                if not self.is_passable(nx, ny): 
                    continue

            if dx !=0 and dy !=0:
                if not (self.is_passable(current.x + dx, current.y) and self.is_passable(current.x, current.y + dy)):
                    continue

                neighbor = Vector2i(nx, ny)
                tentative_g = g_score[(current.x, current.y)] + cost

                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heappush(open_heap, (f_score, neighbor))
                    came_from[(nx, ny)] = current

        return None  # ingen sti fundet

    def reconstruct_path(self, came_from, current):
        path = [current]
        while (current.x, current.y) in came_from:
            current = came_from[(current.x, current.y)]
            path.append(current)
        path.reverse()
        return path

