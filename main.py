import pygame_gui as pgui
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import pygame as pg
import pygame.gfxdraw
import pygame.freetype

pg.init()
pg.freetype.init()

SW, SH = 1280, 690
window = pg.display.set_mode((SW, SH))
ui_manager = pgui.UIManager((SW, SH))
pg.display.set_caption("Reflection of Light")

#logo = pg.image.load("assets/logo.png")
#pg.display.set_icon(logo)

GREYBLUE = "#111e42"
RED = (255, 0, 0)
LIGHTGRAY = (200, 200, 200)
background_color = pg.Color(GREYBLUE)

TILE_SIZE = 6  # WIDTH and HEIGHT of each grid location
MARGIN = 2  # Margin between each cell


class Canvas:
    def __init__(self, size, display_size):
        self.width = size[0]
        self.height = size[1]
        self.display_size = display_size
        self.sPos = ((SW - self.width) // 2, (SH - self.height) // 2)                   # Position of the screen
        self.dsPos = ((SW - self.display_size[0])-20, (SH-self.display_size[1])-15)     # Position of the display
        self.canvas = pg.Surface((self.width, self.height))
        self.canvas.fill((255, 255, 255))
        self.display_canvas = pg.Surface(self.display_size)
  
    def draw(self, window):
        window.blit(self.display_canvas, self.dsPos)


c1 = Canvas((3840, 2160), (int(SW//1.4), int(SH//1.05)))



def createArray():
    global grid
    grid = []
    for row in range(c1.display_size[0]):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(c1.display_size[1]):
            grid[row].append(0)  # Append a cell in each column of the row

def drawGrid():
    for row in range(c1.display_size[0]):
        for column in range(c1.display_size[1]):
            color = LIGHTGRAY
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(c1.display_canvas,
                            color,
                            [(MARGIN + TILE_SIZE) * column+MARGIN,
                            (MARGIN + TILE_SIZE) * row+MARGIN,
                            TILE_SIZE,
                            TILE_SIZE])





run = True
while run:
    delta_time = pg.time.Clock().tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break

        ui_manager.process_events(event)
        
    createArray()
    drawGrid()
    ui_manager.update(delta_time)
    window.fill(background_color)
    c1.draw(window)
    ui_manager.draw_ui(window)

    pg.display.update()

pg.quit()