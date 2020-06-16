from field import *
from canvas import *
from button import *
from tool import *
from toolbar import *
from main_view import *
import utils
import colors
import pygame as pg

class App:
    
    def __init__(self, caption = "Untitled", width = 1200, height = 760, fps = 60):

        pg.init()
        self.caption = caption
        pg.display.set_caption(self.caption)
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.screen = pg.display.set_mode(self.size, pg.HWSURFACE|pg.DOUBLEBUF)
        self.fps = fps
        self.clock = pg.time.Clock()
        self.saved = False
        self.run = True
        self.main_view = MainView(self, width, height, width//1.3)
        self.canvas = list(self.main_view.members.keys())[0]
        self.active_tool = None
        self.mouse_pressed = False
        self.hovered = self.main_view.getHovered((0,0))
        self.clicked = None
        self.mouse_pos = pg.mouse.get_pos()

    def mainLoop(self):
        while self.run:
            self.main_view.display(self.screen, (0,0))
            self.handleEvents()
            pg.display.update()
            self.clock.tick(self.fps)
        pg.quit()

    def handleEvents(self):
        for event in pg.event.get():

                if event.type == pg.QUIT:
                    self.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mouseDown()

                if event.type == pg.MOUSEBUTTONUP:
                    self.mouseUp()

                if event.type == pg.MOUSEMOTION:
                    self.mouseMotion(event.pos, event.rel)

                if event.type == pg.KEYDOWN:
                    self.keyDown(event.key, event.mod)

                if event.type == pg.KEYUP:
                    self.keyUp(event.key, event.mod)

    # Methods triggered by events -------------------------------------------------------------------------------------------

    def mouseMotion(self, pos, rel):
        self.mouse_pos = pos
        self.hovered = self.main_view.getHovered(self.mouse_pos)
        
        if self.clicked is self.canvas and self.canvas.ongoing:
            self.canvas.updateDrawing(pos,rel)

    def mouseDown(self):
        print(f"Mouse pressed down, hovered: {self.hovered}")
        self.mouse_pressed = True
        
        try:
            self.clicked.unclick()
            print("Unclick")
        except AttributeError as e:
            print(e, "nothing to unclick")
    
        self.clicked = self.hovered

        if self.clicked is self.canvas and not self.canvas.ongoing:
            if self.active_tool and self.active_tool.can_draw:
                self.canvas.startDrawing(self.mouse_pos, self.active_tool)
            else:
                print("Active tool cannot draw or no active tool")
        else:
            print(f"Mouse down on {self.clicked}")

    def mouseUp(self):
        self.mouse_pressed = False
        
        if self.clicked == self.hovered:
            self.clicked.click()

        if self.clicked is self.canvas and self.canvas.ongoing:
            self.canvas.endDrawing(self.mouse_pos)

    # IMPORTANT: numLock affects key modifiers (now they are adjusted to unlocked numbers), TODO FIX
    def keyDown(self, key, mod):
        print("Pressed the key", key, "with modifier:", mod)

        if not self.mouse_pressed:
            # quit: Q
            if key == 113:
                self.exit()

            # activate brush: B
            if key == 98:
                self.active_tool = Brush(colors.BLUE, size = 20)

            # undo last changes: U
            if key == 117:
                self.canvas.undoLast()

            # redo last changes: R
            if key == 114:
                self.canvas.redoLast()

            # bigger brush: shift + "+"
            if key == 61 and mod == 2:
                try:
                    self.active_tool.sizeUp()
                except AttributeError:
                    print("Can't resize tool")
            
            # smaller brush: shift + "-"
            if key == 45 and mod == 2:
                try:
                    self.active_tool.sizeDown()
                except AttributeError:
                    print("Can't resize tool")

        else:
            print("can't use keyDown when mouse_pressed") # works wrong with touchpad? TODO fix

    def keyUp(self, key, mod):
        print("Key released:", key, "with modifier: ", mod)
        
    # Other methods -----------------------------------------------------------------------------------------------------------     
    def exit(self):
        self.run = False 
    
    def save(self, askSure = False):
        self.saved = True

    def whenModified(self):
        self.saved = False

    def changeCaption(self, string):
        self.caption = string

if __name__ == "__main__":
    app = App()
    app.mainLoop()


