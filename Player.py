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
  def __init__(self, health : int, speed : float = 0.05, grid_position : Vector2i = Vector2i(int((MAP_WIDTH/2)),int((MAP_HEIGHT/2))), color = (0,0,0)):
    self.grid_position : Vector2i = grid_position
    self.world_position : Vector2f = self.grid_position*TILE_SIZE + Vector2f(TILE_SIZE/2,TILE_SIZE/2) #compensate for grid position being top left coordinate
    self.health = health
    self.speed = speed
    self.color = color
    self.path : list[Vector2i]= []

  def draw(self, screen : pygame.Surface):
    pygame.draw.circle(screen,self.color,(self.world_position.x,self.world_position.y),int(TILE_SIZE/2))
  
  def update(self, dt: float):
    if len(self.path) != 0:
      
      target_cell = self.path[0]
      target_world_pos = target_cell * TILE_SIZE + Vector2f(TILE_SIZE/2, TILE_SIZE/2)

      direction = (target_world_pos - self.world_position).normalize()

      self.world_position += direction * self.speed * dt

      if (target_world_pos - self.world_position).length() < self.speed * dt: # Prevent overshooting
        self.world_position = target_world_pos
        self.grid_position = target_cell
        self.path.pop(0)

