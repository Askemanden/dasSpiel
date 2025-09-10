from vectors import Vector2i
from tile import Tile
import heapq

class pathfinding:
    def __init__(self,tiles:dict[Vector2i, Tile]):
        self.tiles = tiles

    
    def octile_heuristic(self,a: Vector2i ,b: Vector2i) -> int:
        D = 70
        D2 = 99
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)
        return (dx + dy) + 27 * min(dx, dy)

    def neighbors(self, pos:Vector2i):
        directions = [Vector2i(1,0), Vector2i(0,1), Vector2i(-1,0), Vector2i(0,-1),
                      Vector2i(1,1), Vector2i(-1,1), Vector2i(-1,-1), Vector2i(1,-1)]
        for d in directions:
            neighbor = Vector2i(pos.x + d.x, pos.y + d.y)
            if neighbor in self.tiles and self.tiles[neighbor_pos].passable:
                yield neighbor
    
    def find_path(self,start: Vector2i, goal: Vector2i):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.octile_heuristic(start, goal)}

        while open_set:
            current = heapq.heappop(open_set)
            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                tentative_g_score = g_score[current] + (99 if abs(neighbor.x - current.x) + abs(neighbor.y - current.y) == 2 else 70)

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.octile_heuristic(neighbor, goal)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []  # No path found