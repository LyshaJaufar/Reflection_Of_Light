import pygame
from pygame_textinput import TextInput


class Textbox:
    def __init__(self, max_length = -1, action = "",\
        display_text_color = (0, 0, 0), border_size = 1, border_color = (0, 0, 0),\
        color = (255, 255, 255), area = ((0, 0), (0, 0)), spacing=0):
        self.text_object = TextInput(text_color=display_text_color, max_string_length=max_length, font_size=22)
        self.max_length = max_length
        self.action = action
        self.border_size = border_size
        self.border_color = border_color
        self.color = color
        self.display_text_color = display_text_color
        self.area = area
        self.spacing = spacing
        self.active = False

    def update(self, events):
        is_enter_pressed = self.text_object.update(events)
        if self.english_only:
            pass
        if self.numbers_only:
            if self.TextInput.input_string.isdigit():
                pass
        return is_enter_pressed

    def draw(self, main_surface):
        pygame.draw.rect(main_surface, self.border_color, self.area)
        new_area = ((self.area[0][0] + self.border_size, self.area[0][1] + self.border_size),\
                     (self.area[1][0] - (2*self.border_size), self.area[1][1] - (2*self.border_size)))
        
        pygame.draw.rect(main_surface, self.color, new_area)
        text_surf = self.text_object.get_surface()
        new_spot = (new_area[0][0] + self.spacing, new_area[0][1] + ((new_area[1][1] - text_surf.get_height()) / 2))
        main_surface.blit(text_surf, new_spot)

def change_textbox(text, string):
    textbox = text
    textbox.text_object.input_string = string
    textbox.text_object.cursor_position = len(string)
    textbox.text_object.update([])


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
        change_textbox(text, str(int(strX)))
        if abs(int(strX)) > 90:
            if int(strX) < 0:
                strX = "-89"
            else:
                strX = "89"
        change_textbox(text, str(int(strX)))
        # settings.text_location = star_map.coerce_to_center(int(strX),int(strY))
