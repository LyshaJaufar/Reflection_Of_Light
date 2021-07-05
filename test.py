import pygame_gui as pgui
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import pygame as pg
import pygame.gfxdraw
import pygame.freetype

pg.init()
pg.freetype.init()

SW, SH = 1280, 690;
window = pg.display.set_mode((SW, SH))
ui_manager = pgui.UIManager((SW, SH))
pg.display.set_caption("Reflection of Light Simulation")

# logo = pg.image.load("assets/logo.png")
# pg.display.set_icon(logo)

GREYBLUE = "#111e42"
RED = (255, 0, 0)
background_color = pg.Color(GREYBLUE)

class Canvas:
    def __init__(self, size, display_size):
        self.width = size[0]
        self.height = size[1]
        self.display_size = display_size
        self.sPos = ((SW - self.width) // 2, (SH - self.height) // 2)       # position of the surface
        self.dsPos = (SW-display_size[0], (SH-self.display_size[1])//2)    # position of the display window
        self.canvas = pg.Surface((self.width, self.height))
        self.canvas.fill((255, 255, 255))
        self.display_canvas = pg.Surface(self.display_size)

    def draw(self, window):
        window.blit(self.display_canvas, self.dsPos)


c1 = Canvas((3840, 2160), (int(SW//1.8), int(SH//1.8)))


run = True
while run:
    delta_time = pg.time.Clock().tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break


        if event.type == pg.USEREVENT:
            c1.blit_to_canvas()

        ui_manager.process_events(event)

    ui_manager.update(delta_time)
    window.fill(background_color)
    c1.draw(window)
    ui_manager.draw_ui(window)
    pg.display.update()

pg.quit()