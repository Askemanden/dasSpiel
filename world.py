from vectors import Vector2i, Vector2f
from biome import Biome
from feature import Feature
from tile import Tile
from random import randint
from perlin_noise import PerlinNoise
from settings import *
import pygame

class Chunk:
    def __init__(self, biome : Biome, features : list[Feature], tiles : dict[Vector2i, Tile]):
        self.biome = biome
        self.features = features
        self.tiles = tiles
    
    def __str__(self):
        return f"biome : {self.biome}, features : {self.features}, tiles {self.tiles}"


class World:
    def __init__(self):
        self.seed : int = randint(0,9999)
        self.changes : list = []
        self.biomeNoise = PerlinNoise(octaves = 4, seed = self.seed)
        self.current_chunk_pos : Vector2i = Vector2i(0,0)

        self.chunk : Chunk = self.generate_chunk()
        self.current_biome : Biome = self.chunk.biome
        self.features : list[Feature] = self.chunk.features
        self.real_tiles : dict[Vector2i, Tile] = self.chunk.tiles


    def generate_chunk(self) -> Chunk:
        seed = int(self.seed * self.current_chunk_pos.length())
        feature_noise = PerlinNoise(octaves = 2, seed = seed)
        biome = Biome(self.biomeNoise([self.current_chunk_pos.x + 0.1,self.current_chunk_pos.y + 0.1])) # Add 0.1 to compensate for perlin noise values being 0 at integer coordinates
        features : list[Feature]= []
        for i in range(0, MAP_WIDTH, FEATURE_FREQUENCY):
            for j in range(0, MAP_HEIGHT, FEATURE_FREQUENCY):
                noise_val = feature_noise([i / MAP_WIDTH, j / MAP_HEIGHT])
                features.append(Feature(Vector2i(i, j), noise_val,biome.type,self.current_chunk_pos,self.seed))
        tiles_list : list[Tile] = []

        for feature in features:
            tiles_list.extend(feature.tiles)
        
        tiles : dict[Vector2i, Tile] = {}

        for tile in tiles_list:
            tiles[tile.position] = tile
        
        return Chunk(biome, features, tiles)

    def draw(self, surface : pygame.Surface):
        self.current_biome.draw(surface)
        for tile in self.real_tiles.values():
            tile.draw(surface)



        
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE, MAP_HEIGHT*TILE_SIZE))
    pygame.display.set_caption("World Draw Test")

    world = World()

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear screen
        world.draw(screen)      # Draw the world
        pygame.display.flip()   # Update display
        clock.tick(60)          # Limit to 60 FPS

    pygame.quit()