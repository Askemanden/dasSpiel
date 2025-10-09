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
import json
import enum
from signals import*

running = True


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

def start():
    pass

def quit():
    global running
    running = False

"""                                         
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░   ░    ░░░░░   ░        ░░░░░░     ░░░░░
▒   ▒  ▒   ▒▒▒   ▒   ▒▒▒▒▒▒▒▒▒   ▒▒▒▒   ▒▒
▒   ▒   ▒   ▒▒   ▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   
▓   ▓   ▓▓   ▓   ▓       ▓▓▓   ▓▓▓▓▓▓▓▓   
▓   ▓   ▓▓▓  ▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   
▓   ▓   ▓▓▓▓  ▓  ▓   ▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓
█   █   ██████   █   ███████████     █████
██████████████████████████████████████████
"""

class UI_info():                                                        # Basisklasse for alle info og udvidelsesklasser til et komponent.
    def __init__ (self):
        pass
    def update(self):
        pass
    def event_handling(self, event):
        pass
    def draw(self, screen):
        pass


class UI_component_placement_info(UI_info):
    def __init__(self, x, y, width, height, anchor_x = "left", anchor_y = "top"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.anchor_x = anchor_x
        self.anchor_y = anchor_y

class UI_component_color_info(UI_info):
    def __init__(self, primary_color = (100, 149, 237), secondary_color = (0, 70, 148), accent_color = (227, 209, 120)):
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.accent_color = accent_color
        self.primary_complementary_color = (255 - primary_color[0], 255 - primary_color[1], 255 - primary_color[2])
        self.secondary_complementary_color = (255 - secondary_color[0], 255 - secondary_color[1], 255 - secondary_color[2])



"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░         ░   ░░░░░░   ░           ░         ░    ░░░░░   ░░░      ░░░   ░░░░░     ░░░░░░    ░░░░░   ░░░      ░░
▒   ▒▒▒▒▒▒▒▒   ▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒  ▒   ▒▒▒   ▒   ▒▒▒▒   ▒   ▒▒▒   ▒▒▒▒   ▒▒▒  ▒   ▒▒▒   ▒   ▒▒▒▒   
▒   ▒▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒   ▒▒   ▒▒   ▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒   ▒   ▒   ▒▒   ▒▒   ▒▒▒▒▒▒
▓       ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓       ▓▓▓   ▓▓   ▓   ▓▓▓▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓   ▓   ▓▓▓▓   ▓▓▓▓
▓   ▓▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓  ▓   ▓▓▓▓▓▓▓   ▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓  ▓   ▓▓▓▓▓▓▓   ▓
▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓  ▓  ▓   ▓▓▓▓   ▓   ▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓  ▓  ▓   ▓▓▓▓   
█         █   ██████   █████   █████         █   ██████   ███      ███   █████     ██████   ██████   ███      ██
████████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""

class UI_component_text(UI_info):
    def __init__(self, component, text = "Hej verden"):
        self.component = component
        
        self.text = text
        self.font = pygame.font.SysFont('Arial', 20)
        self.bold = False

    def get_text_color(self):
        if isinstance(self.component.color_info, UI_component_color_info):
            return self.component.color_info.secondary_complementary_color
        else:
            return self.component.parent_box.color_info.secondary_complementary_color

    def update(self):
        if self.component.hovered:
            self.bold = True

    def draw(self, screen):
        image = self.font.render(self.text, True, self.get_text_color())
        self.text_rect = image.get_rect()

        text_surface = self.font.render(self.text, True, self.get_text_color(), None)
        screen.blit(text_surface, (self.component.rect.x + 5 + (0.5 * (self.component.rect.width - self.text_rect.width)), self.component.rect.y + self.component.rect.height * 0.2))

class UI_button_extension(UI_info):
    def __init__(self, component, function = intet):
        self.function = function
        self.component = component

    def event_handling(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.component.rect.collidepoint(event.pos):
                self.function()

    def update(self):
        if self.component.rect.collidepoint(pygame.mouse.get_pos()):   
            self.component.hovered = True
        else:
            self.component.hovered = False

"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░   ░░░░░   ░   ░░░░░░░   ░░░   ░░░░░░░     ░░░░░░   ░░░░░░░   ░        ░░░░░░░     ░░░░░░    ░░░░░   ░         ░    ░░░░░   ░           
▒   ▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒   ▒▒   ▒▒▒▒▒▒   ▒▒▒▒   ▒▒▒  ▒   ▒▒▒    ▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒   ▒▒▒  ▒   ▒▒▒   ▒   ▒▒▒▒▒▒▒  ▒   ▒▒▒   ▒▒▒▒▒   ▒▒▒▒
▒   ▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒   ▒ ▒   ▒   ▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒   ▒   ▒   ▒▒   ▒   ▒▒▒▒▒▒▒   ▒   ▒▒   ▒▒▒▒▒   ▒▒▒▒
▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓  ▓  ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓   ▓▓   ▓        ▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓   ▓   ▓       ▓▓▓   ▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓
▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓  ▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓  ▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓  ▓   ▓▓▓▓▓   ▓▓▓▓
▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓  ▓  ▓   ▓▓▓▓▓▓▓   ▓▓▓▓  ▓  ▓▓▓▓▓   ▓▓▓▓
███      ████   ███████   █████   █████     ██████   ███████   █   ████████████     ██████   ██████   █         █   ██████   █████   ████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""

class UI_component:                                         # Basisklasse for alle UI komponenter til et UI_element.
    def __init__(self, placement_info: UI_component_placement_info = UI_info(), color_info: UI_component_color_info = UI_info()):
        self.color_info = color_info
        self.hovered = False
        self.placement_info = placement_info
        self.text = UI_info()
        self.button = UI_info()
        self.parent_box = None

        self.rect = pygame.Rect(0, 0, 10, 10)

    def update_color(self):
        if not isinstance(self.color_info, UI_component_color_info):
            self.color_info = self.parent_box.color_info

    def update(self):
        self.color_info.update()
        self.placement_info.update()
        self.text.update()
        self.button.update()

    def event_handling(self, event):
        #self.text.event_handling(event)
        self.button.event_handling(event)

    def draw(self, screen):
       
        if not isinstance(self.color_info, UI_component_color_info):
           color_source = self.parent_box.color_info
        else:
            color_source = self.color_info
        
        #pygame.draw.rect(screen, (100, 100, 100), self.rect)
        if self.hovered:
            #brighter_color = (min(color_source.secondary_color[0] + 40, 255), min(color_source.secondary_color[1] + 40, 255), min(color_source.secondary_color[2] + 40, 255))
            brighter_color = color_source.accent_color
            pygame.draw.rect(screen, brighter_color, self.rect)
        else:
            pygame.draw.rect(screen, color_source.secondary_color, self.rect)
        self.text.draw(screen)


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░   ░░░░░   ░   ░░░░░░░         ░   ░░░░░░░░         ░   ░░░░░░░   ░         ░    ░░░░░   ░           
▒   ▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒  ▒   ▒▒▒    ▒   ▒▒▒▒▒▒▒  ▒   ▒▒▒   ▒▒▒▒▒   ▒▒▒▒
▒   ▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒   ▒ ▒   ▒   ▒▒▒▒▒▒▒   ▒   ▒▒   ▒▒▒▒▒   ▒▒▒▒
▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓       ▓▓▓   ▓▓▓▓▓▓▓▓       ▓▓▓   ▓▓   ▓▓   ▓       ▓▓▓   ▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓
▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓  ▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓  ▓   ▓▓▓▓▓   ▓▓▓▓
▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓▓  ▓  ▓▓▓▓▓   ▓▓▓▓
███      ████   ███████         █          █         █   ███████   █         █   ██████   █████   ████
██████████████████████████████████████████████████████████████████████████████████████████████████████
"""

class alignment(enum.Enum):
    horizontal = 0
    vertical = 1

class UI_element:                                                       # Basisklasse for alle UI elementer.
    def __init__(self, placement : UI_component_placement_info):
        self.screen_position_x = placement.x
        self.screen_position_y = placement.y
        self.rect = pygame.Rect(placement.x, placement.y, placement.width, placement.height)                           # Basisklasse har en rektangel.
        self.color_info = UI_info()

    def update(self):
        pass

    def move(self, x : int, y : int):
        pass

    def draw(self, screen : pygame.Surface):
        pass

class screen_box (UI_element):                                       # En boks på skærmen der kan indeholde knapper og items.
    def __init__(self, placement : UI_component_placement_info, color : UI_component_color_info):
        super().__init__(placement)
        self.screen_position_x = placement.x - placement.width * 0.5
        self.screen_position_y = placement.y - placement.height * 0.5
        self.rect = pygame.Rect(self.screen_position_x, self.screen_position_y, placement.width, placement.height)

        self.border_width = 8
        
        self.color_info = color
        self.border_color = color.secondary_color
       
        self.components = []
        self.number_of_buttons = 0                                      # Antallet af automatisk placerede knapper i listen af containere. Bruges til at arrangere knapperne jævnt.

    def create_UIcomponent(self, color : UI_component_color_info = UI_info(), placement_info : UI_component_placement_info = UI_info(), text = "", function = None):
        component = UI_component(placement_info, color)
        component.parent_box = self
        text_object = UI_component_text(component, text)
        component.text = text_object
        if function != None:
            button_object = UI_button_extension(component, function)
            component.button = button_object

        self.components.append(component)
        self.place_all_components()

    def add_UIcomponent(self, container):                               # Tilføjer et UI-komponent til listen af komponenter.
        if container in self.components:
            return False
        if isinstance(container.placement_info, UI_component_placement_info):
            if (container.placement_info.x + container.placement_info.width > self.rect.width or container.placement_info.y + container.placement_info.height > self.rect.height):
                return False                                                # Containeren kan ikke tilføjes, da den ikke kan være i screen_boxen.
            if container.placement_info.x < 0 and container.placement_info.anchor_x != "center" or container.placement_info.y < 0 and container.placement_info.anchor_y != "center": 
                return False
        container.parent_box = self
        self.components.append(container)
        self.place_all_components()
        return True
    
    def count_buttons(self):                                            # Tæller antallet af automatisk placerede knapper i listen af containere.
        count = 0
        for container in self.components:
            if not isinstance(container.placement_info, UI_component_placement_info) and isinstance(container.button, UI_button_extension):
                count += 1
        self.number_of_buttons = count

    def rainbow(self):
        temporary_colors : UI_component_color_info = self.color_info
        temporary_colors.primary_color = self.color_info.accent_color
        temporary_colors.accent_color = self.color_info.primary_color
        self.color_info = temporary_colors
        self.update()

    def remove_container(self, container):                              # Fjerner en container fra listen af containere.
        pass # TODO

    def update(self):                                                   # Opdaterer tilstanden af screen_boxen og dens containere.
                                                                        # update kalder ikke den matematiktunge place_all_buttons, da den kun behøver at blive kaldt når en container tilføjes eller fjernes, eller kassen flyttes.
        for container in self.components:
           container.update()

    def place_component(self, component, automatic_button_index):       # sætter x og y positionen for en knap baseret på dens placering KUN i forhold til andre af dens type.
                                                                        # Bredden og højden beregnes af screen_boxen, da dette er lettere.
        if isinstance(component.placement_info, UI_component_placement_info):   # Component er en knap med manuel layout info.

            if component.placement_info.anchor_x == "center":
                component.rect.x = self.rect.x + (self.rect.width - component.placement_info.width) * 0.5 + component.placement_info.x
            else:
                component.rect.x = self.rect.x + component.placement_info.x

            if component.placement_info.anchor_y == "center":
                component.rect.y = self.rect.y + (self.rect.height - component.placement_info.height) * 0.5 + component.placement_info.y
            else:
                component.rect.y = self.rect.y + component.placement_info.y

        else:
            if isinstance(component.button, UI_button_extension):
                button_height = component.rect.height
                button_width = component.rect.width
                component.rect.x = self.rect.x + self.border_width + automatic_button_index * (button_width + self.border_width)
                component.rect.y = self.rect.y + self.rect.height - self.border_width - button_height

            elif isinstance(component, label):
                component.rect.x = self.rect.x + self.border_width
                component.rect.y = self.rect.y + self.border_width
                component.rect.width = self.rect.width - self.border_width * 2
                component.rect.height = self.rect.height - (self.border_width * 2 + 40 * 1.2) # 40 er standarden for knaphøjde. TODO: Gør dette dynamisk baseret på screen_boxens højde.
    
    def place_all_components(self):
        self.count_buttons()
        automatic_button_index = 0

        for container in self.components:

            if not isinstance(container.placement_info, UI_component_placement_info):
                if isinstance(container.button, UI_button_extension):    # Automatisk placeret knap.
                    container.rect.width = (self.rect.width - self.border_width * (self.number_of_buttons + 1)) / self.number_of_buttons
                    container.rect.height = 40 # Standard højde for knapper. TODO: Gør dette dynamisk baseret på screen_boxens højde.
                    automatic_button_index += 1
                else:
                    pass
                    # Det er ikke en automatisk placeret knap.
                    #TODO implementer håndtering af komponenter uden placement_info der ikke er en knap
            else:
                container.rect.width = container.placement_info.width
                container.rect.height = container.placement_info.height

            self.place_component(container, automatic_button_index - 1)  # -1 fordi indexet er blevet forøget efter placeringen af knappen.
                
    def move(self, x, y):
        self.screen_position_x = x - self.rect.width * 0.5
        self.screen_position_y = y - self.rect.height * 0.5
        self.rect.topleft = (self.screen_position_x, self.screen_position_y)
        self.place_all_components()

    def event_handler(self, event):
        for component in self.components:
            component.event_handling(event)

    def draw(self, screen):
        # Tegner en boks med en kant. Kanten er border_width pixels bred.
        border_rect = pygame.Rect(self.rect.left - self.border_width, self.rect.top - self.border_width, self.rect.width + self.border_width * 2, self.rect.height + self.border_width * 2)
        pygame.draw.rect(screen, self.border_color, border_rect)
        pygame.draw.rect(screen, self.color_info.primary_color, self.rect)

        # Tegner alle UI-komponenter i boksen.
        # For nu arrangeres alle knapper, vandret i bunden af boksen. Lidt ligesom Windows pop-up menuer.
        # Alle andre UI-komponenter arrangeres lodret i toppen af boksen, og der kan scrolles gennem dem.
        for container in self.components:
            container.draw(screen)





#########################################################################################

class button(UI_component):
    def __init__(self, function = intet, layout_info : UI_component_placement_info = None):
        self.on_click = function

        self.color = (100, 149, 237)                        # Knapper er blå.

        self.is_hovered = False

        self.layout_info = layout_info

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


class label(UI_component):
    def __init__(self, text = "Tekst", font_size = 30, layout_info : UI_component_placement_info = None):
        super().__init__()

        self.layout_info = layout_info
        self.parent_box = None
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont('Arial', self.font_size)
        self.background_color = (255, 255, 255)                    # Baggrunden til tekst er hvid. Som standard bliver baggrunden ikke tegnet.
        self.text_color = (0, 0, 0)                     # Tekst farve er sort.
        self.padding = 10

        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()

        self.on_click = intet

    def set_text(self, new_text):
        self.text = new_text

    def background_color(self, new_color):
        self.background_color = new_color
    
    def text_color(self, new_color):
        self.text_color = new_color
    
    def update(self):
        pass

    def draw(self, screen):
        #pygame.draw.rect(screen, self.background_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color, None)
        screen.blit(text_surface, (self.rect.x + self.padding, self.rect.y + self.padding))

"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░   ░░░░      ░░░░░░░     ░░░░░░    ░░░░░   ░░░░░░░   ░░░░░░░   ░░░░░░░  ░░░░░░░░░░░     ░░░░░   
▒▒▒▒▒▒   ▒▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒   ▒▒▒  ▒   ▒▒▒   ▒▒▒▒▒▒▒  ▒   ▒▒▒    ▒▒▒▒▒▒  ▒  ▒▒▒▒▒▒▒  ▒▒▒▒   ▒▒▒   
▒▒▒▒▒▒   ▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒   ▒▒   ▒▒▒▒▒▒▒   ▒   ▒ ▒   ▒▒▒▒▒  ▒▒   ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒   
▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓▓▓▓   ▓▓▓   ▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓   
▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓  ▓   ▓▓▓▓▓▓▓   ▓▓▓  ▓▓   ▓▓▓       ▓   ▓▓▓   ▓▓▓      ▓   
▓  ▓▓▓   ▓▓   ▓▓▓▓   ▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓  ▓  ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓  ▓▓▓   
██     ██████      ███████     ██████   ██████   ███████   ███████   █   █████████   ███      █████   
██████████████████████████████████████████████████████████████████████████████████████████████████████
"""

main_menu = {   # skabelon til at skabe en menu
    "color_info": [198, 198, 198, 0, 167, 205, 134, 189, 0],
    "placement_info": [400, 300, 300, 250, "center", "center"],
    "components": {
        0: {
            "color_info": None,
            "placement_info": None,
            "text": "Afslut",
            "button_function": "quit"
        },
        1: {
            "color_info": None,
            "placement_info": None,
            "text": "Spil",
            "button_function": "Start"
        },
        2: {
            "color_info": [22, 124, 198, 43, 80, 170, 79, 168, 111],
            "placement_info": [0, -40, 140, 60, "center", "center"],
            "text": "Das Spiel",
            "button_function": None
        }
    }
}


#with open("menu.json", "w", encoding="utf-8") as f:
#    json = json.dump(main_menu, f, indent=4)



function_map = {
    "quit": quit,
    "start": start,
    None: None
}

menus = []

def create_menu_from_json(json_data):
    placement_info = UI_component_placement_info(
        json_data["placement_info"][0],
        json_data["placement_info"][1],
        json_data["placement_info"][2],
        json_data["placement_info"][3],
        json_data["placement_info"][4],
        json_data["placement_info"][5]
        )
    color_info = UI_component_color_info(
        (json_data["color_info"][0], json_data["color_info"][1], json_data["color_info"][2]),
        (json_data["color_info"][3], json_data["color_info"][4], json_data["color_info"][5]),
        (json_data["color_info"][6], json_data["color_info"][7], json_data["color_info"][8])
    )

    menu = screen_box(placement_info, color_info)

    for index in range(len(json_data["components"])):
        

        index_component = json_data["components"][f"{index}"]
        component_color = UI_info()
        component_placement = UI_info()
        component_text = None

        if  index_component["color_info"] != None:
            component_color = UI_component_color_info(
                (index_component["color_info"][0], index_component["color_info"][1], index_component["color_info"][2]),
                (index_component["color_info"][3], index_component["color_info"][4], index_component["color_info"][5]),
                (index_component["color_info"][6], index_component["color_info"][7], index_component["color_info"][8])
            )
        if index_component["placement_info"] != None:
            component_placement = UI_component_placement_info(
                index_component["placement_info"][0],
                index_component["placement_info"][1],
                index_component["placement_info"][2],
                index_component["placement_info"][3],
                index_component["placement_info"][4],
                index_component["placement_info"][5]
            )
        if index_component["text"] != None:
            component_text = index_component["text"]

        if index_component["button_function"] != None:
            func_key = index_component["button_function"]
            func_key = function_map.get(func_key, None)
        else:
            func_key = None

        menu.create_UIcomponent(component_color, component_placement, component_text, func_key)
    menus.append(menu)

# Testkode
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    with open("menu.json", "r", encoding="utf-8") as f:
       menu_data = json.load(f)
    create_menu_from_json(menu_data)

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Window Partitioner")

    #kasse = screen_box(UI_component_placement_info(300, 200, 400, 250, "Askeslaske"), UI_component_color_info((198, 198, 198), (0, 167, 205), (134, 189, 0)))

    #label1 = label("Dette er en test af Window Partitioner", 27)
    #kasse.add_UIcomponent(label1)

    #kasse.create_UIcomponent(UI_info(), UI_info(), "Askeslaske", quit)
    #kasse.create_UIcomponent(UI_info(), UI_info(), "Akselslakel", quit)
    #kasse.create_UIcomponent(UI_info(), UI_component_placement_info(0, 0, 80, 40, "center", "center"), "Charlie")


    while running:
        #popup_menu.update()
        #kasse.update()
        for box in menus:
            box.update()
        

        for event in pygame.event.get():                    # Håndterer begivenheder som lukning af vindue og museklik.
            
            if event.type == pygame.QUIT:
                running = False
            
            #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                #kasse.move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            else:
                for box in menus:
                    box.event_handler(event)

            #elif event.type == pygame.MOUSEBUTTONDOWN:      # Håndterer museklik.
            #    mouse_pos = event.pos

        for box in menus:
            box.draw(screen)
        #screen_box.draw(screen)
        pygame.display.flip()
    pygame.quit()
    quit()