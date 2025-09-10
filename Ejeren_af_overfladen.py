import pygame

class Game:
    def __init__(self,):
        pygame.init()
        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Game')
        self.clock = pygame.time.Clock()

        self.running = False


    def setup(self):
        pass

    def game_loop(self):
        while self.running:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
