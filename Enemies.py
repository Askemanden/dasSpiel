"""
Enemies
"""
from settings import*
from vectors import*
from pathfind import astar
from world import World
from tile import Tile
from random import randint
import pygame

def get_valid_spawn_position(real_tiles : dict[Vector2i, Tile]) -> Vector2i:
    while True:
        pos = Vector2i(randint(1, MAP_WIDTH - 1), randint(1, MAP_HEIGHT - 1))
        tile = real_tiles.get(pos)

        if tile == None or tile.passable:
            return pos

class Enemies:
    def __init__(self, color, state, world: World, health: int, 
                 damage: int, speed: float, home_radius: int, 
                 home_center: Vector2i, grid_position: Vector2i):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.color = color
        self.state = state
        self.grid_position = get_valid_spawn_position(world.real_tiles)
        self.home_center = self.grid_position
        self.world_position: Vector2f = self.grid_position*TILE_SIZE + Vector2f(TILE_SIZE/2, TILE_SIZE/2)
        self.subtargets: list[Vector2f] = []
    
    def draw(self, screen : pygame.Surface):
        pygame.draw.circle(screen,self.color,(self.world_position.x,self.world_position.y),int(TILE_SIZE/2))
        if not DEBUG_MODE:
            return
        def draw_path_segment(start: Vector2f, end: Vector2f):
             pygame.draw.line(screen, (0, 255, 255), (start.x, start.y), (end.x, end.y), 3)
        previous_position = self.world_position
        for i in self.subtargets:
            draw_path_segment(previous_position, i)
            previous_position = i

    def set_path(self, path: list[Vector2i], final_world_position: Vector2f):
        if path == None:
            return
        path.pop(0)
        self.path = path
        self.final_world_position = final_world_position
        self.subtargets.clear()

        if not path:
            return

        previous_cell_position = self.grid_position
        for i, cell in enumerate(path):
            cell_center = cell * TILE_SIZE + Vector2f(TILE_SIZE/2, TILE_SIZE/2)

            if previous_cell_position is not None:
                corner = self._shared_point(previous_cell_position, cell)
                if corner is not None:
                    self.subtargets.append(corner)

            self.subtargets.append(cell_center)

            previous_cell_position = cell

        self.subtargets.pop()
        self.subtargets.append(self.final_world_position)

    def _shared_point(self, a: Vector2i, b: Vector2i) -> Vector2f | None:
        dx, dy = b.x - a.x, b.y - a.y
        if abs(dx) > 1 or abs(dy) > 1:
            return None  # not neighbors

        # Base corner is the center of cell a
        ax, ay = a.x * TILE_SIZE + TILE_SIZE/2, a.y * TILE_SIZE + TILE_SIZE/2
        return Vector2f(ax + dx * TILE_SIZE/2, ay + dy * TILE_SIZE/2)
    
    def newTarget(self, params : list[list[int,int],World]):
        worldTargetList = params[0]
        worldTarget = Vector2f(worldTargetList[0],worldTargetList[1])
        target: Vector2i = Vector2i(int(worldTarget.x // TILE_SIZE), int(worldTarget.y // TILE_SIZE))

        world: World = params[1]
        real_tiles : list[Tile] = world.real_tiles.values()
        blocked : list[Vector2i] = []
        for tile in real_tiles:
            if not tile.passable:
                blocked.append(tile.position)

        path = astar(self.grid_position,target,blocked)

        self.set_path(path,worldTarget)

        # Did not consume the event
        return False
    
    def update(self, dt: float):
        if not self.subtargets:
            return

        target = self.subtargets[0]
        move_vec = target - self.world_position
        if move_vec.length() > 0:
            direction = move_vec.normalize()
            self.world_position += direction * self.speed * dt

        # Snap if close enough
        if (target - self.world_position).length() < self.speed * dt:
            self.world_position = target
            self.subtargets.pop(0)
            if len(self.path) > 0 and self.world_position == (self.path[0]*TILE_SIZE + Vector2f(TILE_SIZE/2, TILE_SIZE/2)):
                self.grid_position = self.path.pop(0)
 
    
    
    