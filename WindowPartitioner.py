import pygame
from vectors import Vector2f
import enum

class screen_box:
    def __init__(self, x, y, width, height):
        self.screen_position_x = x - width * 0.5
        self.screen_position_y = y - height * 0.5
        self.rect = pygame.Rect(self.screen_position_x, self.screen_position_y, width, height)

        self.border_width = 8
        self.border_color = (17, 37, 78)

        self.color = (120,105,105)
       
        self.containers = []

    def add_container(self, container):                                 # Tilføjer en container til listen af beholdere.
        if container.on_click == intet and container.type == button:    # Hvis containeren ikke har en funktion, så kan den ikke tilføjes.
            return False
        
        self.containers.append(container)                               # En container kan være en knap eller en holder til en item.
        self.update_container_rects()
        return True
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        for container in self.containers:
            if container.rect.collidepoint(mouse_pos):
                container.is_hovered = True
            else:
                container.is_hovered = False

    def update_container_rects(self):

        for container in self.containers:
            length = len(self.containers)

            if container.container_type == container_type.button:
                container.rect.width = (self.rect.width - self.border_width * 2) / (length - self.border_width * 2)
                container.rect.height = 30  # Arbitrær værdi for knap højde.
                index = self.containers.index(container)
                container.rect.topleft = (self.rect.top + (self.rect.height - self.border_width * 2),self.rect.left + self.border_width + index * container.rect.width)
            
                

    def move(self, x, y):
        self.screen_position_x = x - self.rect.width * 0.5
        self.screen_position_y = y - self.rect.height * 0.5
        self.rect.topleft = (self.screen_position_x, self.screen_position_y)
        self.update_container_rects()


    def draw(self, screen):
        # Tegner en boks med en kant. Kanten er border_width pixels bred.
        pygame.draw.rect(screen, self.border_color, self.rect)
        middle_rect = pygame.Rect(self.rect.left + self.border_width, self.rect.top + self.border_width, self.rect.width - self.border_width * 2, self.rect.height - self.border_width * 2)
        pygame.draw.rect(screen, self.color, middle_rect)

        # Tegner alle containere i boksen.
        # For nu arrangeres alle containere, der er knapper, vandret i bunden af boksen. Lidt ligesom Windows pop-up menuer.
        # Alle andre containere arrangeres lodret i toppen af boksen, og der kan scrolles gennem dem.
        self.update()
        for container in self.containers:
            container.draw(screen)

def intet():
    pass

def quit():
    pygame.quit()
    exit()



class container_type(enum.Enum):
    item = 0
    button = 1

class container:
    def __init__(self, type, function = intet):
        self.on_click = function
        self.container_type = type
        self.is_hovered = False

        if self.container_type == container_type.button:    # Knapper er blå.
            self.color = (100, 149, 237)
        else:
            self.color = (70, 130, 180)                     # Items er mørkeblå.

        self.rect = pygame.Rect(0, 0, 10, 10)               # Burde ikke blive ændret af andre end screen_box
                                                            # således at alle knapper i en screen_box kan blive jævnt fordelt, og ens størrelse.

    def draw(self, screen):
        if self.is_hovered:
            brighter_color = (min(self.color[0] + 40, 255), min(self.color[1] + 40, 255), min(self.color[2] + 40, 255))
            pygame.draw.rect(screen, brighter_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

# Testkode
if __name__ == ("__main__"):
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Window Partitioner")
    running = True
    screen_box = screen_box(200, 200, 300, 300)

    button = container(container_type.button, pygame.quit)
    screen_box.add_container(button)


    while running:
        for event in pygame.event.get():                    # Håndterer begivenheder som lukning af vindue og museklik.
            
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:      # Håndterer museklik.
                mouse_pos = event.pos
                screen_box.update()
                for container in screen_box.containers:
                    if container.rect.collidepoint(mouse_pos):

                        container.on_click()
                    
            
            #elif


        screen_box.draw(screen)
        pygame.display.flip()
    pygame.quit()