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

        self.grid = []
        self.tile_size = 6  # WIDTH and HEIGHT of each grid location
        self.margin = 2     # Margin between each cell

        self.clicked = False
        self.position = dict()
        self.pos = (0,0)
        self.column = 0
        self.row = 0

    def createArray(self):
        for row in range(c1.display_size[0]):               # Add an empty array that will hold each cell in this row
            self.grid.append([])
            for column in range(c1.display_size[1]):        # Append a cell in each column of the row
                self.grid[row].append(0)  

    def drawGrid(self):
        self.createArray()
        for row in range(c1.display_size[0]):
            self.row = row
            for column in range(c1.display_size[1]):
                self.column = column
                color = LIGHTGRAY
                if self.grid[row][column] == 1:
                    color = RED
                pygame.draw.rect(c1.display_canvas,
                                color,
                                [(self.margin + self.tile_size) * column+self.margin,
                                (self.margin + self.tile_size) * row+self.margin,
                                self.tile_size,
                                self.tile_size])

    def clickCell(self):
        self.clicked = True
        self.pos = pygame.mouse.get_pos()
        self.column = self.pos[0] // self.display_size[1]-(self.tile_size + self.margin)
        self.row = self.pos[1] // self.display_size[0] - (self.tile_size + self.margin)

        self.grid[self.row][self.column] = 1
        self.grid[self.row][-self.column] = 2
        print("Click ", self.pos, "Grid cooridnates: ", self.row, self.column)
        self.position[self.pos] = (self.row, self.column)    

    def draw(self, window):
        window.blit(self.display_canvas, self.dsPos)
        self.drawGrid()


c1 = Canvas((3840, 2160), (int(SW//1.4), int(SH//1.05)))


run = True
while run:
    delta_time = pg.time.Clock().tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            c1.clickCell()

        ui_manager.process_events(event)

    ui_manager.update(delta_time)
    window.fill(background_color)
    c1.draw(window)
    ui_manager.draw_ui(window)

    pg.display.update()

pg.quit()