"""
                        mm                      mm                                                                         mm           mm                                          
*@@@@*     @     *@@@*  @@                    *@@@                                   *@@@***@@m                     @@     @@    @@     @@                                          
  *@@     m@@     m@                            @@                                     @@   *@@m                    @@           @@                                                 
   @@m   m@@@m   m@   *@@@  *@@@@@@@@m     m@**@@@    m@@*@@m *@@*    m@    *@@*       @@   m@@  m@*@@m  *@@@m@@@ @@@@@@ *@@@  @@@@@@ *@@@    m@@*@@m *@@@@@@@@m    mm@*@@ *@@@m@@@ 
    @@m  @* @@m  @*     @@    @@    @@   m@@    @@   @@*   *@@  @@   m@@@   m@         @@@@@@@  @@   @@    @@* **   @@     @@    @@     @@   @@*   *@@  @@    @@   m@*   @@  @@* ** 
    !@@ @*  *@@ @*      !@    @!    @@   @!@    @!   @@     @@   @@ m@  @@ m@          @@        m@@@!@    @!       @@     !@    @@     !@   @@     @@  @!    @@   !@******  @!     
     !@@m    !@@m       !@    @!    !@   *!@    @!   @@     !@    @@@    @!!           @!       @!   !@    @!       @!     !@    @!     !@   @@     !@  @!    !@   !@m    m  @!     
     !!@!*   !!@!*      !!    !!    !!   !!!    !!   !@     !!    !@!!   !:!           @!        !!!!:!    !!       !!     !!    !!     !!   !@     !!  !!    !!   !!******  !!     
     !!!!    !!!!       !!    !!    !!   *:!    !:   !!!   !!!    !!!    !:!           !!       !!   :!    !:       !!     !!    !!     !!   !!!   !!!  !!    !!   :!!       !:     
      :       :       : : : : :::  :!: :  : : : ! :   : : : :      :      :          :!:!:      :!: : !: : :::      ::: :: : :   ::: :: : :   : : : : : :::  :!: :  : : :: : :::    
                                                                                                                                                                                    
"""




import pygame
from vectors import*
import enum
from signals import*

running = True

class alignment(enum.Enum):
    horizontal = 0
    vertical = 1

class UI_element:                                                       # Basisklasse for alle UI elementer.
    def __init__(self, x, y):
        self.screen_position_x = x
        self.screen_position_y = y
        self.rect = pygame.Rect(x, y, 10, 10)                           # Basisklasse har en rektangel.
        self.color = (255, 255, 255)                                    # Basisklasse har en farve.

    def update(self):
        pass

    def move(self, x : int, y : int):
        pass

    def draw(self, screen : pygame.Surface):
        pass

class screen_box (UI_element):                                       # En boks på skærmen der kan indeholde knapper og items.
    def __init__(self, x, y, width, height, button_alignment = alignment.horizontal):
        super().__init__(x, y)
        self.screen_position_x = x - width * 0.5
        self.screen_position_y = y - height * 0.5
        self.rect = pygame.Rect(self.screen_position_x, self.screen_position_y, width, height)

        self.border_width = 8
        self.border_color = (17, 37, 78)

        self.color = (120,105,105)
       
        self.containers = []
        self.number_of_buttons = 0
        self.number_of_manuals = 0
        self.button_alignment = button_alignment

    def add_container(self, container):                                 # Tilføjer en container til listen af beholdere.
        self.containers.append(container)                               # En container kan være en knap eller en holder til en item.
        self.sort_containers()
        self.update_container_rects()
        return True
    
    def add_manual_container(self, container, x, y, width, height):     # Tilføjer en container uden automatisk at opdatere dens rektangel. Sætter en container på en manuel position i forhold til kassen.
        
        if container in self.containers:
            return False
        if x < 0 or y < 0 or width <= 0 or height <= 0:
            return False
        if x + width > self.rect.width or y + height > self.rect.height:
            return False
        container.x = x
        container.y = y
        container.width = width
        container.height = height
        container.rect.x = x
        container.rect.y = y
        container.rect.width = width
        container.rect.height = height
        container.manual = True
        self.containers.append(container)
        self.sort_containers()
        self.update_container_rects()
        return True
    
    def sort_containers(self):
        self.number_of_buttons = 0
        self.number_of_manuals = 0                                      # Sorterer containere i boksen efter deres type. Automatisk placerede containere kommer før manuelt placerede containere.
        temporary_list = self.containers.copy()
        button_list = []
        manual_list = []
        self.containers.clear()
        for container in temporary_list:
            if container.container_type == container_type.button and not container.manual:
                button_list.append(container)
                self.number_of_buttons += 1
            elif container.manual:
                manual_list.append(container)
                self.number_of_manuals += 1
        self.containers = button_list
        for container in manual_list:
            self.containers.append(container)



    def update(self):                                                   # Opdaterer tilstanden af screen_boxen og dens containere.
        mouse_pos = pygame.mouse.get_pos()                              # update kalder ikke den matematiktunge updtate_container_rects, da den kun behøver at blive kaldt når en container tilføjes eller fjernes, eller kassen flyttes.

        for container in self.containers:
            if container.rect.collidepoint(mouse_pos):
                container.is_hovered = True
            else:
                container.is_hovered = False

    def update_container_rects(self):

        for container in self.containers:
            if container.manual:
                container.rect.x = self.rect.x + self.border_width + container.x
                container.rect.y = self.rect.y + container.y + self.border_width

            elif self.button_alignment == alignment.horizontal:
               if container.container_type == container_type.button:
                index = self.containers.index(container)

                container.rect.width = (self.rect.width - (self.number_of_buttons + 3) * self.border_width) / self.number_of_buttons
                container.rect.height = 40  # Arbitrær værdi for knap højde.
                
                container.rect.x = self.rect.x + self.border_width * 2 + index * (container.rect.width + self.border_width)
                container.rect.y = self.rect.y + self.rect.height - self.border_width * 2 - container.rect.height

            elif self.button_alignment == alignment.vertical:
                if container.container_type == container_type.button:
                    index = self.containers.index(container)

                    container.rect.width = self.rect.width * 0.5 - self.border_width * 2
                    container.rect.height = 40  # Arbitrær værdi for knap højde.
                    
                    container.rect.x = self.rect.x + self.border_width
                    container.rect.y = self.rect.y + self.rect.height - self.border_width * 2 - (self.number_of_buttons - index) * (container.rect.height + self.border_width)
            
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
    global running
    running = False


class container_type(enum.Enum):
    item = 0
    button = 1
    image = 2

class container:
    def __init__(self, type, function = intet):
        self.on_click = function
        self.container_type = type

        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10

        self.manual = False
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
    pygame.font.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Window Partitioner")

    screen_box = Askeslaske = screen_box(220, 220, 400, 200)

    Askeslaske_knap1 = container(container_type.button, quit)
    Askeslaske_knap2 = container(container_type.button, quit)
    Askeslaske_knap3 = container(container_type.button, quit)
    Askeslaske_knap4 = container(container_type.button, quit)

    Askeslaske.add_manual_container(Askeslaske_knap4, 20, 20, 30, 30)
    Askeslaske.add_container(Askeslaske_knap1)
    Askeslaske.add_container(Askeslaske_knap2)
    Askeslaske.add_container(Askeslaske_knap3)
   



    while running:
        #popup_menu.update()
        Askeslaske.update()
        

        for event in pygame.event.get():                    # Håndterer begivenheder som lukning af vindue og museklik.
            
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:      # Håndterer museklik.
                mouse_pos = event.pos
                
                for container in Askeslaske.containers:

                    if container.rect.collidepoint(mouse_pos):
                        container.on_click()
                    
            
            #elif


        Askeslaske.draw(screen)
        #screen_box.draw(screen)
        pygame.display.flip()
    pygame.quit()
    quit()