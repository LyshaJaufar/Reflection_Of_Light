import pygame
import random
pygame.init()

class Textbox:
    def __init__(self, max_length = -1, action = "",\
                display_text_color = (0, 0, 0), border_size = 1, border_color = (0, 0, 0),\
                color = (255, 255, 255), area = ((0, 0), (0, 0)), spacing=0):
        self.text_object = ""
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

        self.text_object += str(current)
        if e.key == pygame.K_RETURN:
            print(self.text_object)
            self.text_object = ""
        #print(self.text_object)
        return e.key




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

# show the pygame window
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame Example")

text = Textbox(action="angleOfIncidence",area=((30, 235), (200, 50)), border_size=2, spacing=1, max_length=15)

# loop around until the user presses escape or Q
looping = True
while looping:
    # choose a random colour
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # fill the screen in the random colour
    screen.fill((red, green, blue))
    pygame.display.flip()

    # wait for a key to be pressed
    key = text.update()

    # stop looping if the user presses Q or escape
    if key == pygame.K_q or key == pygame.K_ESCAPE:
        looping = False


pygame.quit()