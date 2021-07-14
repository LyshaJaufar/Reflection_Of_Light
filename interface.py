import pygame
import random
from pygame_textinput import TextInput
pygame.init()

class Textbox:
    def __init__(self, max_length = -1, action = "",\
                display_text_color = (0, 0, 0), border_size = 1, border_color = (0, 0, 0),\
                color = (255, 255, 255), area = ((0, 0), (0, 0)), spacing=0):
        self.text_object = TextInput(text_color=display_text_color, max_string_length=max_length, font_size=22)
        self.text = ""
        self.max_length = max_length
        self.action = action
        self.border_size = border_size
        self.border_color = border_color
        self.color = color
        self.display_text_color = display_text_color
        self.area = area
        self.spacing = spacing
        self.active = False

    def update(self):
        e = pygame.event.wait()
        while e.type != pygame.KEYDOWN:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                return pygame.K_ESCAPE

        current = ""
        if e.key == pygame.K_0 or e.key == pygame.K_1 or e.key == pygame.K_2 or e.key == pygame.K_3\
        or e.key == pygame.K_4 or e.key == pygame.K_5 or e.key == pygame.K_6 or e.key == pygame.K_7\
        or e.key == pygame.K_8 or e.key == pygame.K_9:
            current =  e.key-48
            print('here')

        self.text += str(current)
        print('also here')
        if e.key == pygame.K_RETURN:
            print("success")
            self.active = False
            return self.text
        #print(self.text_object)
 




    def draw(self, main_surface):
        pygame.draw.rect(main_surface, self.border_color, self.area)
        new_area = ((self.area[0][0] + self.border_size, self.area[0][1] + self.border_size),\
                     (self.area[1][0] - (2*self.border_size), self.area[1][1] - (2*self.border_size)))
        
        pygame.draw.rect(main_surface, self.color, new_area)
        text_surf = self.text_object.get_surface()
        new_spot = (new_area[0][0] + self.spacing, new_area[0][1] + ((new_area[1][1] - text_surf.get_height()) / 2))
        main_surface.blit(text_surf, new_spot)




def perform_action(text, action):
    if action == "angleOfIncidence":
        strX = ""
        posX = text.text_object.input_string
        print("test", posX)

        for char in posX:
            if char.isdigit() or char == "-":
                strX += char
        if not strX:
            strX = "-69"
        # change_textbox(text, str(int(strX)))
        if abs(int(strX)) > 90:
            if int(strX) < 0:
                strX = "-89"
            else:
                strX = "89"
        # change_textbox(text, str(int(strX)))
        # settings.text_location = star_map.coerce_to_center(int(strX),int(strY))



text = Textbox(action="angleOfIncidence",area=((30, 235), (200, 50)), border_size=2, spacing=1, max_length=15)




pygame.quit()