import pygame_gui as pgui
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import pygame as pg
import pygame.gfxdraw
import pygame.freetype
import math
from interface import *

pg.init()
pg.freetype.init()

SW, SH = 1280, 690
window = pg.display.set_mode((SW, SH))
ui_manager = pgui.UIManager((SW, SH))
pg.display.set_caption("Reflection of Light")

#logo = pg.image.load("assets/logo.png")
#pg.display.set_icon(logo)
angleInputted = False

GREYBLUE = "#111e42"
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTGRAY = (200, 200, 200)
DARKGRAY = (30, 30, 30)
background_color = pg.Color(GREYBLUE)



xs_font = pg.freetype.Font("Basic-Regular.ttf", 12)
mid_font = pg.freetype.Font("Basic-Regular.ttf", 18)
big_font = pg.freetype.Font("Basic-Regular.ttf", 35)
large_font = pg.freetype.Font("Basic-Regular.ttf", 40)

fonts = [xs_font, mid_font, big_font, large_font]
font_sizes = [12, 18, 35, 40]

def text_to_screen(window, text, color, pos, font_size=12):
    font_used = fonts[font_sizes.index(font_size)]
    font_used.render_to(window, pos, text, color)

class Canvas:
    def __init__(self, size, display_size):
        self.width = size[0]
        self.height = size[1]
        self.display_size = display_size
        self.left_margin = 35
        self.upper_margin = 25
        self.sPos = ((SW - self.width) // 2, (SH - self.height) // 2)   # Position of the screen
        self.dsPos = ((SW - self.display_size[0])-self.left_margin, 
                    (SH-self.display_size[1])-self.upper_margin)        # Position of the display     
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
        self.reflectedRays = []
        self.finalIncidentRays = []
        self.finalReflectedRays = []
        self.generate = False

    def createArray(self):
        row = self.dsPos[1]
        column = self.dsPos[0]
        for i in range(row, self.display_size[0]):               # Add an empty array that will hold each cell in this row
            self.grid.append([])
            for j in range(column, self.display_size[1]):        # Append a cell in each column of the row
                self.grid[abs(row-i)].append(0)  

    def drawGrid(self):
        row = self.dsPos[1]
        column = self.dsPos[0]


        for i in range(row, self.display_size[0]):
            for j in range(column, self.display_size[1]):
                color = LIGHTGRAY
                if self.grid[abs(row-i)][abs(column-j)] == 1:
                    color = GREEN
                if self.grid[abs(row-i)][abs(column-j)] == 2 and self.generate == True:
                    color = RED
                    self.grid[abs(row-i)][abs(column-j)] = 3
                if self.grid[abs(row-i)][abs(column-j)] == 3:
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

        # Draw coords for the grid
        column_coord_position = self.dsPos[0]
        row_coord_position = self.dsPos[1]
        index = 0
        font_size = 2
        for i in range(column_coord_position+font_size, SW-self.left_margin, self.tile_size+font_size):       
            text_to_screen(window=window, text=str(index), color=RED, pos=(i, self.dsPos[1]-self.tile_size))
            index += 1

        index = 0
        for i in range(row_coord_position+font_size, (SH-self.upper_margin), self.tile_size+font_size):
            text_to_screen(window=window, text=str(index), color=RED, pos=(self.dsPos[0]-self.tile_size, i))
            index += 1

        text_to_screen(window=window, text="REFLECTION OF LIGHT", color=RED, pos=(575, 25), font_size=40)
        text_to_screen(window=window, text="ANGLE OF INCIDENCE", color=RED, pos=(50, 210), font_size=18)

    def clickCell(self):
        self.clicked = True
        self.pos = pygame.mouse.get_pos()

        self.column = (self.pos[0]//(self.tile_size+self.margin)) - (self.dsPos[0]//(self.tile_size + self.margin))
        self.row = (self.pos[1]//(self.tile_size+self.margin)) - (self.dsPos[1]//(self.tile_size + self.margin))

        if self.column <= (self.totalColumns//2) and self.column >= 0 and self.row >= 0 and self.row < 38:
            if self.grid[self.row][self.column] == 0:
                self.grid[self.row][self.column] = 1
                self.grid[self.row][self.totalColumns - self.column] = 2
                self.incidentRays.append(IncidentRay(x1=self.pos[0], y1=self.pos[1]))
                self.reflectedRays.append(ReflectedRay(y1=IncidentRay(x1=self.pos[0], 
                                        y1=self.pos[1]).Y2,x2=self.pos[0], y2=self.pos[1]))

            # Removing accidental clicks
            else:
                self.grid[self.row][self.column] = 0
                self.grid[self.row][self.totalColumns - self.column] = 0
        
        self.position[self.pos] = (self.row, self.column)    
        

    def initialDraw(self, window):
        window.blit(self.display_canvas, self.dsPos)
        self.drawGrid()
        if self.generate == True: 
            for ray in self.incidentRays:
                ray.draw(window)
                self.finalIncidentRays.append(ray)
                for ray in self.reflectedRays:
                    ray.draw(window)
                    self.finalReflectedRays.append(ray)
        self.generate = False

    def draw(self, window):
        for ray in self.finalIncidentRays:
            ray.draw(window)
            for ray in self.finalReflectedRays:
                ray.draw(window)

c1 = 0
class IncidentRay():
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = c1.dsPos[0] + (c1.display_size[0]/2)
        self.y2 = ((self.x2 - self.x1) / slope) + self.y1

        self.Y2 = self.y2
        self.y2 = self.y2 if (self.y2 < 660) else 660
  
    def draw(self, screen):
        pygame.draw.line(screen, RED, (self.x1, self.y1), (self.x2, self.y2), width=2)

class ReflectedRay(IncidentRay):
    def __init__(self, y1, x2, y2):
        self.x1 = c1.dsPos[0] + (c1.display_size[0]/2)
        self.x2 = x2
        self.y1 = y1
        self.y2 = ((self.x2 - self.x1) / (slope * -1)) + self.y1

        self.y2CoordOfExtendedLine = y2
        self.x2CoordOfExtendedLine = ((slope*-1) * (self.y2CoordOfExtendedLine - self.y1)) + self.x1

        self.y1 = self.y1 if (self.y1 < 660) else 660
        self.y2 = self.y2 if (self.y2 < 660) else 660
         
    def draw(self, screen):
        pygame.draw.line(screen, BLUE, (self.x1, self.y1), (self.x2, self.y2), width=2)
        pygame.draw.line(screen, DARKGRAY, (self.x1, self.y1), 
                        (self.x2CoordOfExtendedLine, self.y2CoordOfExtendedLine), width=1)

        
c1 = Canvas((3840, 2160), (int(SW//1.3), int(SH//1.19)))
c1.createArray()

def generate_ui():
    ui_manager.clear_and_reset()
    lm = 30     # Left margin

    random_generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(lm, 125, 200, 50),
                                                    text="Generate", manager=ui_manager,
                                                    object_id="generate_button")

def updateAngle(angle):
    loop = True
    angle.text = ""
    while loop:

        e = pygame.event.wait()
        while e.type != pygame.KEYDOWN:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                return pygame.K_ESCAPE

        if e.key == pygame.K_0 or e.key == pygame.K_1 or e.key == pygame.K_2 or e.key == pygame.K_3\
        or e.key == pygame.K_4 or e.key == pygame.K_5 or e.key == pygame.K_6 or e.key == pygame.K_7\
        or e.key == pygame.K_8 or e.key == pygame.K_9 or e.key == pygame.K_BACKSPACE or pygame.K_DELETE:
            if e.key == pygame.K_BACKSPACE or e.key == pygame.K_DELETE:
                if len(angle.text) > 0:
                    angle.text = angle.text.rstrip(angle.text[-1])

            if e.key != pygame.K_BACKSPACE and e.key != pygame.K_DELETE and e.key != pygame.K_RETURN:
                angle.text +=  str(e.key-48)
                text.text_object.update(angle.text)                

        if e.key == pygame.K_RETURN:
            if int(angle.text) > 89:
                angle.text = 89
            angle.active = False
            loop = False
            return angle.text
    

textbox = Textbox(action="angleOfIncidence",area=((30, 235), (200, 50)), border_size=2, spacing=1, max_length=15)
text = Textbox(action="angleOfIncidence",area=((112, 245), (50, 35)), border_size=0, spacing=1, max_length=15)
generate_ui()


generate = False
run = True
while run:
    delta_time = pg.time.Clock().tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse =  pygame.mouse.get_pos()
            if textbox.area[0][0] <= mouse[0] <= textbox.area[0][0]+textbox.area[1][0] and\
            textbox.area[0][1] <= mouse[1] <= textbox.area[0][1]+textbox.area[1][1]:
                text.active = True
                angle = updateAngle(text)

                # Angle of incidence for all the lines
                angle_in_radians = math.radians(int(angle))
                slope = (math.tan(angle_in_radians))
                angleInputted = True

            if angleInputted:
                c1.clickCell()


        if event.type == pg.USEREVENT:
            if event.user_type == pgui.UI_BUTTON_PRESSED:
                if event.ui_object_id == "generate_button":
                    generate = True
                    c1.generate = True

        ui_manager.process_events(event)

        
    ui_manager.update(delta_time)
    window.fill(background_color)
    c1.initialDraw(window)
    c1.draw(window)
    textbox.draw(window)
    text.draw(window)
    ui_manager.draw_ui(window)


    pg.display.update()

pg.quit()