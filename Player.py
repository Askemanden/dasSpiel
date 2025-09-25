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

class player:
  def __init__(self, health : int, speed : float = 10, grid_position : Vector2i = Vector2i(0,0), square_position : Vector2f = Vector2f(0,0), color = (30,20,230)):
    self.square_position_relative_to_center : Vector2f = square_position
    self.grid_position : Vector2i = grid_position
    self.health = health
    self.speed = speed
    self.color = color
    self.path : list[Vector2i]= []

  def draw(self, screen : pygame.Surface):
    position = self.grid_position*TILE_SIZE + self.square_position
    pygame.draw.circle(screen,self.color,(position.x,position.y),10)
  
  def update(self, screen : pygame.Surface, dt : float):
    if len(self.path) != 0:
      direction_to_next_cell = self.grid_position.direction_to(self.path[0])
    
  
