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


    def draw(self, main_surface):
        pygame.draw.rect(main_surface, self.border_color, self.area)
        new_area = ((self.area[0][0] + self.border_size, self.area[0][1] + self.border_size),\
                     (self.area[1][0] - (2*self.border_size), self.area[1][1] - (2*self.border_size)))
        
        pygame.draw.rect(main_surface, self.color, new_area)
        text_surf = self.text_object.get_surface()
        new_spot = (new_area[0][0] + self.spacing, new_area[0][1] + ((new_area[1][1] - text_surf.get_height()) / 2))
        main_surface.blit(text_surf, new_spot)

pygame.quit()