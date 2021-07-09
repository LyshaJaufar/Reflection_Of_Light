import pygame_gui as pgui
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import pygame as pg
import pygame.gfxdraw
import pygame.freetype
import math

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
GREEN = (0, 255, 0)
LIGHTGRAY = (200, 200, 200)
background_color = pg.Color(GREYBLUE)

# Angle of incidence for all the lines
angle = 50
angle_in_radians = math.radians(angle)
slope = (math.tan(angle_in_radians))


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
        self.tile_size = 15  # WIDTH and HEIGHT of each grid location
        self.margin = 2     # Margin between each cell

        self.clicked = False
        self.position = dict()
        self.pos = (0,0)
        self.column = 0
        self.row = 0
        self.totalColumns = 57

        self.incidentRays = []

    def createArray(self):
        row = self.dsPos[1]
        column = self.dsPos[0]
        for i in range(row, c1.display_size[0]):               # Add an empty array that will hold each cell in this row
            self.grid.append([])
            for j in range(column, c1.display_size[1]):        # Append a cell in each column of the row
                self.grid[abs(row-i)].append(0)  

    def drawGrid(self):
        row = self.dsPos[1]
        column = self.dsPos[0]

        for i in range(row, c1.display_size[0]):
            for j in range(column, c1.display_size[1]):
                color = LIGHTGRAY
                if self.grid[abs(row-i)][abs(column-j)] == 1:
                    color = GREEN
                if self.grid[abs(row-i)][abs(column-j)] == 2:
                    color = RED
                pygame.draw.rect(self.display_canvas,
                                color,
                                [(self.margin + self.tile_size) * (abs(column-j))+self.margin,
                                (self.margin + self.tile_size) * (abs(row-i))+self.margin,
                                self.tile_size,
                                self.tile_size])
        # Draw mirror on the grid
        pg.draw.line(self.display_canvas, RED, ((self.display_size[0]//2)+1, 1), 
                    ((self.display_size[0]/2)+1, self.display_size[1]),2)

    def clickCell(self):
        self.clicked = True
        self.pos = pygame.mouse.get_pos()

        self.column = (self.pos[0]//(self.tile_size+self.margin)) - (self.dsPos[0]//(self.tile_size + self.margin))
        self.row = (self.pos[1]//(self.tile_size+self.margin)) - (self.dsPos[1]//(self.tile_size + self.margin) + 1)

        if self.column <= (self.totalColumns//2):
            if self.grid[self.row][self.column] == 0:
                self.grid[self.row][self.column] = 1
                self.grid[self.row][self.totalColumns - self.column] = 2
                self.incidentRays.append(IncidentRay(x1=self.pos[0], y1=self.pos[1]))

            # Removing accidental clicks
            else:
                self.grid[self.row][self.column] = 0
                self.grid[self.row][self.totalColumns - self.column] = 0
        
        print("Click ", self.pos, "Grid cooridnates: ", self.row, self.column)
        self.position[self.pos] = (self.row, self.column)    
        

    def draw(self, window):
        window.blit(self.display_canvas, self.dsPos)
        self.drawGrid()
        for ray in self.incidentRays:
            ray.draw(window)

c1 = 0
class IncidentRay():
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = c1.dsPos[0] + (c1.display_size[0]/2)
        self.y2 = ((self.x2 - self.x1) / slope) + self.y1
  
    def draw(self, screen):
        pygame.draw.line(screen, RED, (self.x1, self.y1), (self.x2, self.y2), width=2)
        
c1 = Canvas((3840, 2160), (int(SW//1.3), int(SH//1.1)))
c1.createArray()


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