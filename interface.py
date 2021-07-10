import pygame, math

class Label:
    def __init__(self, text = "", text_color = (0, 0, 0), background_color = (255, 255, 255), 
                font_size = 25, pos = (0, 0)):
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Times New Roman', font_size)
        self.pos = pos
        self.background_color = background_color

    def draw(self, main_surface):
        text_surf = self.font.render(self.text, True, self.text_color, self.background_color)
        main_surface.blit(text_surf, self.pos)

Label(text = "Input Text:", font_size = 32, pos = (25, 85))