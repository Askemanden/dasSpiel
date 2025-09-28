"""
              mm                                        
*@@@***@@m  *@@@                                        
  @@   *@@m   @@                                        
  @@   m@@    @@   m@*@@m  *@@*   *@@*  mm@*@@ *@@@m@@@ 
  @@@@@@@     !@  @@   @@    @@   m@   m@*   @@  @@* ** 
  @@          !@   m@@@!@     @@ m!    !@******  @!     
  @!          !@  @!   !@      @@!     !@m    m  @!     
  @!          !!   !!!!:!      @!!     !!******  !!     
  !!          :!  !!   :!      !!:     :!!       !:     
:!:!:       : : : :!: : !:     !!       : : :: : :::    
                             ::!                        
                           :::                          
"""
from settings import*
from vectors import*
import pygame

class Player:
  def __init__(self, health: int, speed: float = 0.05,
               grid_position: Vector2i = Vector2i(int(MAP_WIDTH/2), int(MAP_HEIGHT/2)),
               color=(0,0,0)):
    self.grid_position: Vector2i = grid_position
    self.world_position: Vector2f = self.grid_position*TILE_SIZE + Vector2f(TILE_SIZE/2, TILE_SIZE/2)
    self.health = health
    self.speed = speed
    self.color = color
    self.path: list[Vector2i] = []
    self.final_world_position: Vector2f = self.world_position
    self.subtargets: list[Vector2f] = []   # expanded path in world coords

  
  def draw(self, screen : pygame.Surface):
     pygame.draw.circle(screen,self.color,(self.world_position.x,self.world_position.y),int(TILE_SIZE/2))

  def set_path(self, path: list[Vector2i], final_world_position: Vector2f):
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

