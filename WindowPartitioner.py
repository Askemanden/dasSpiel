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
        self.number_of_buttons = 0                                      # Antallet af automatisk placerede knapper i listen af containere. Bruges til at arrangere knapperne jævnt.
        self.button_alignment = button_alignment


    def add_button(self, container):                                    # Tilføjer en container til listen af beholdere.
        if container in self.containers or isinstance(container, manually_placed_button):
            return False
        self.containers.append(container)                               # En container kan være en knap eller en holder til en item.
        self.place_all_buttons()
        return True
    
    def add_manual_button(self, container, x, y, width, height):        # Tilføjer en container uden automatisk at opdatere dens rektangel. Sætter en container på en manuel position i forhold til kassen.
        
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
        self.containers.append(container)
        self.place_all_buttons()
        return True
    
    def count_buttons(self):                                            # Tæller antallet af automatisk placerede knapper i listen af containere.
        count = 0
        for container in self.containers:
            if isinstance(container, button):
                count += 1
        self.number_of_buttons = count

    def remove_container(self, container):                              # Fjerner en container fra listen af containere.
        pass # TODO

    def update(self):                                                   # Opdaterer tilstanden af screen_boxen og dens containere.
                                                                        # update kalder ikke den matematiktunge place_all_buttons, da den kun behøver at blive kaldt når en container tilføjes eller fjernes, eller kassen flyttes.
        for container in self.containers:
           container.update()

    def place_button(self, button, automatic_button_index):             # sætter x og y positionen for en knap baseret på dens placering KUN i forhold til andre af dens type.
                                                                        # Bredden og højden beregnes af screen_boxen, da dette er lettere.
        if isinstance(button, manually_placed_button):
            button.rect.x = self.rect.x + button.x
            button.rect.y = self.rect.y + button.y
        
        else:
            button_height = button.rect.height
            button_width = button.rect.width

            if self.button_alignment == alignment.horizontal:
                button.rect.x = self.rect.x + self.border_width * 2 + automatic_button_index * (button_width + self.border_width)
                button.rect.y = self.rect.y + self.rect.height - self.border_width * 2 - button_height

            else:
                pass    # TODO: Implementer vertikal placering af knapper.
    
    def place_all_buttons(self):
        self.count_buttons()
        automatic_button_index = 0

        for container in self.containers:

            if isinstance(container, button):
                container.rect.width = (self.rect.width - self.border_width * (self.number_of_buttons + 3)) / self.number_of_buttons    # Der lægges 3 til fordi screen_boxen har en kant, som også skal tages i betragtning, sammen med mellemrum mellem knapperne.
                container.rect.height = 40 # Standard højde for knapper. TODO: Gør dette dynamisk baseret på screen_boxens højde.
                automatic_button_index += 1

            self.place_button(container, automatic_button_index - 1)  # -1 fordi indexet er blevet forøget efter placeringen af knappen.
                
    def move(self, x, y):
        self.screen_position_x = x - self.rect.width * 0.5
        self.screen_position_y = y - self.rect.height * 0.5
        self.rect.topleft = (self.screen_position_x, self.screen_position_y)
        self.place_all_buttons()


    def draw(self, screen):
        # Tegner en boks med en kant. Kanten er border_width pixels bred.
        pygame.draw.rect(screen, self.border_color, self.rect)
        middle_rect = pygame.Rect(self.rect.left + self.border_width, self.rect.top + self.border_width, self.rect.width - self.border_width * 2, self.rect.height - self.border_width * 2)
        pygame.draw.rect(screen, self.color, middle_rect)

        # Opdaterer knappernes positioner, og tegner dem
        

        # Tegner alle containere i boksen.
        # For nu arrangeres alle containere, der er knapper, vandret i bunden af boksen. Lidt ligesom Windows pop-up menuer.
        # Alle andre containere arrangeres lodret i toppen af boksen, og der kan scrolles gennem dem.
        for container in self.containers:
            container.draw(screen)

#TODO: reimplementer popup_menu
""" 
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
"""

def intet():
    pass

def quit():
    global running
    running = False

class UI_component:                                         # Basisklasse for alle UI komponenter til et UI_element.
    def __init__(self):
        pass
    
    def update(self):
        pass

    def draw(self, screen):
        pass

class button(UI_component):
    def __init__(self, function = intet):
        self.on_click = function

        self.color = (100, 149, 237)                        # Knapper er blå.

        self.is_hovered = False

        self.rect = pygame.Rect(0, 0, 10, 10)               # Burde ikke blive ændret af andre end screen_box
                                                            # således at alle knapper i en screen_box kan blive jævnt fordelt, og ens størrelse.

    def update(self):
        pygame.mouse.get_pos()
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_hovered = True
        else:
            self.is_hovered = False

    def draw(self, screen):
        if self.is_hovered:
            brighter_color = (min(self.color[0] + 40, 255), min(self.color[1] + 40, 255), min(self.color[2] + 40, 255))
            pygame.draw.rect(screen, brighter_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)


class manually_placed_button(UI_component):
    def __init__(self, function):
        self.on_click = function
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10

        self.is_hovered = False

        self.color = (100, 149, 237)                     # Knapper er blå.

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)     # Burde ikke blive ændret af andre end screen_box
                                                         # således at alle knapper i en screen_box kan blive jævnt fordelt, og ens størrelse.
    def update(self):
        pygame.mouse.get_pos()
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_hovered = True
        else:
            self.is_hovered = False
    
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

    knap1 = button(quit)
    knap2 = button(intet)
    knap3 = button(intet)
    knap4 = manually_placed_button(quit)
    Askeslaske.add_button(knap1)
    Askeslaske.add_button(knap2)
    Askeslaske.add_button(knap3)
    Askeslaske.add_manual_button(knap4, 50, 50, 10, 10)


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