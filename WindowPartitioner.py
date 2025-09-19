import pygame
from vectors import Vector2f
import enum

class alignment(enum.Enum):
    horizontal = 0
    vertical = 1

class screen_box:
    def __init__(self, x, y, width, height, button_alignment = alignment.horizontal):
        self.screen_position_x = x - width * 0.5
        self.screen_position_y = y - height * 0.5
        self.rect = pygame.Rect(self.screen_position_x, self.screen_position_y, width, height)

        self.border_width = 8
        self.border_color = (17, 37, 78)

        self.color = (120,105,105)
       
        self.containers = []
        self.button_alignment = button_alignment

    def add_container(self, container):                                 # Tilføjer en container til listen af beholdere.
        self.containers.append(container)                               # En container kan være en knap eller en holder til en item.
        self.update_container_rects()
        return True
    
    def update(self):                                                   # Opdaterer tilstanden af screen_boxen og dens containere.
        mouse_pos = pygame.mouse.get_pos()                              # update kalder ikke den matematiktunge updtate_container_rects, da den kun behøver at blive kaldt når en container tilføjes eller fjernes, eller kassen flyttes.

        for container in self.containers:
            if container.rect.collidepoint(mouse_pos):
                container.is_hovered = True
            else:
                container.is_hovered = False

    def update_container_rects(self):

        for container in self.containers:
            length = len(self.containers)

            if self.button_alignment == alignment.horizontal:
               if container.container_type == container_type.button:
                index = self.containers.index(container)

                container.rect.width = (self.rect.width - (length + 3) * self.border_width)/ length
                container.rect.height = 40  # Arbitrær værdi for knap højde.
                
                container.rect.x = self.rect.x + self.border_width * 2 + index * (container.rect.width + self.border_width)
                container.rect.y = self.rect.y + self.rect.height - self.border_width * 2 - container.rect.height

            elif self.button_alignment == alignment.vertical:
                if container.container_type == container_type.button:
                    index = self.containers.index(container)

                    container.rect.width = self.rect.width * 0.5 - self.border_width * 2
                    container.rect.height = 40  # Arbitrær værdi for knap højde.
                    
                    container.rect.x = self.rect.x + self.border_width
                    container.rect.y = self.rect.y + self.rect.height - self.border_width * 2 - (length - index) * (container.rect.height + self.border_width)
            
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


class popup_menu_types(enum.Enum):
    OK_CANCEL = 0
    YES_NO = 1
    QUIT = 2

class popup_menu(screen_box):
    def __init__(self, x, y, width, height, type):
        super().__init__(x, y, width, height, button_alignment = alignment.horizontal)
        self.type = type
        if self.type == popup_menu_types.OK_CANCEL:
            pass
        elif self.type == popup_menu_types.YES_NO:
            pass
        elif self.type == popup_menu_types.QUIT:
            
            return_button = container(container_type.button, intet)
            return_button.color = (34, 139, 34)  # Grøn farve for return knappen.
            self.add_container(return_button)

            quit_button = container(container_type.button, quit)
            quit_button.color = (220, 20, 60)  # Rød farve for quit knappen.
            self.add_container(quit_button)
            




def intet():
    pass

def quit():
    pygame.quit()
    quit()

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

    #button1 = container(container_type.button, quit)
    #screen_box.add_container(button1)
    #button2 = container(container_type.button, quit)
    #screen_box.add_container(button2)

    #text_box = text_box(400, 250, 300, 200, "Dette er en test")

    popup_menu = popup_menu(400, 250, 300, 200, popup_menu_types.QUIT)


    while running:
        popup_menu.update()
        

        for event in pygame.event.get():                    # Håndterer begivenheder som lukning af vindue og museklik.
            
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:      # Håndterer museklik.
                mouse_pos = event.pos
                
                for container in popup_menu.containers:

                    if container.rect.collidepoint(mouse_pos):
                        container.on_click()
                    
            
            #elif


        popup_menu.draw(screen)
        pygame.display.flip()
    pygame.quit()
    quit()