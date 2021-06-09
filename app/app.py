# GIT TEST
from field import *
from canvas import *
from button import *
from tool import *
from toolbar import *
import utils
import colors
import pygame as pg

class App:
    """
    Main class used to run the program.
    
    Attributes:

        caption (str): caption on top bar of the window
        size ((int, int)): size of the window
        screen: Surface created by pygame.display.set_mode() representing everything inside the pygame window
        fps (int): number of frames per second passed to pygame.Clock.tick()
        clock: pygame Clock object used by the program
        run (bool): value indicating whether program should end (False => end)
        canvas: object of type Canvas used to represent the drawing area
        toolbar: object of type MainToolbar used to represent the toolbar area
        main_view: object of type MainView used to display all visible parts of the screen
        active_tool: reference to selected tool
        mouse_pressed (bool)
        hovered: reference to the object representing the part of the screen currently hovered by mouse
        clicked: reference to the object representing the part of the screen clicked by user
        mouse_pos: current position of the mouse on the screen

    """
    
    def __init__(self, caption = "PyPaint", width = 1200, height = 800, fps = 60):
        """
        Inits the pygame module and creates a new instance of App with all attributes set to default values. 
        """

        canvas_width = width // 1.3
        
        pg.init()
        self.caption = caption
        pg.display.set_caption(self.caption)
        self.size = (width, height)
        self.screen = pg.display.set_mode(self.size, pg.HWSURFACE|pg.DOUBLEBUF)
        self.fps = fps
        self.clock = pg.time.Clock()
        self.run = True
        self.canvas = Canvas(canvas_width, height)
        self.toolbar = MainToolbar(self, width - canvas_width, height)
        self.main_view = MainView(width, height, self.canvas, self.toolbar)
        self.active_tool = None
        self.mouse_pressed = False
        self.hovered = self.main_view.getHovered((0,0))
        self.clicked = None
        self.mouse_pos = pg.mouse.get_pos()

    def mainLoop(self):
        """
        Runs the program as long as App.run attribute is True.
        """
        while self.run:
            self.main_view.display(self.screen, (0,0))
            self.handleEvents()
            pg.display.update()
            self.clock.tick(self.fps)
        pg.quit()

    def handleEvents(self):
        """
        Calls App's methods triggered by events detected by pygame.event.get()
        """
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

    def mouseMotion(self, pos, rel):
        """
        Updates App.mouse_pos and App.hovered attributes and calls updateDrawing() if drawing is ongoing.
        """
        self.mouse_pos = pos
        self.hovered = self.main_view.getHovered(self.mouse_pos)
    
        if isinstance(self.clicked, Canvas) and self.clicked.ongoing:
            self.clicked.updateDrawing(pos,rel)

    def mouseDown(self):
        """
        Sets App.mouse_pressed to True, unclicks currently clicked object and calls startDrawing() if the canvas is hovered.
        """
        self.mouse_pressed = True
        if self.hovered is not self.clicked:
            try:
                self.clicked.unclick()
            except AttributeError:
                pass
        
            self.clicked = self.hovered

        if isinstance(self.clicked, Canvas) and not self.clicked.ongoing:
            if self.active_tool and self.active_tool.can_draw:
                self.clicked.startDrawing(self.mouse_pos, self.active_tool)
            else:
                print("Active tool cannot draw or no active tool")
        
        else:
            print(f"Mouse down on {self.clicked}")

    def mouseUp(self):
        """
        Sets App.mouse_pressed to False; tries to call the click method on the hovered object; calls endDrawing()
        """
        self.mouse_pressed = False
        
        if self.clicked == self.hovered:
            try:
                self.clicked.click()
            except AttributeError:
                pass

        if isinstance(self.clicked, Canvas) and self.clicked.ongoing:
            self.clicked.endDrawing(self.mouse_pos)

    def keyDown(self, key, mod):
        # print("Pressed the key", key, "with modifier:", mod)

        if not self.mouse_pressed:
            # quit: Q
            if key == 113:
                self.exit()

            # activate brush: B
            if key == 98:
                self.active_tool = tool.brush1

            # undo last changes: U
            if key == 117:
                self.undo()

            # redo last changes: R
            if key == 114:
                self.redo()

            # bigger brush: shift + "+"
            if key == 61 and mod == 2:
                self.sizeToolUp()
            
            # smaller brush: shift + "-"
            if key == 45 and mod == 2:
                self.sizeToolDown()
            
            # save: S
            if key == 115:
                self.save()        

    def keyUp(self, key, mod):
        pass
        
    def exit(self):
        self.run = False 
    
    def save(self, askSure = False):
        s = self.canvas.getCurrent()
        pg.image.save(s, './saves/new.png')

    def undo(self):
        """
        Calls undoLast() method of the canvas.
        """
        self.canvas.undoLast()

    def redo(self):
        self.canvas.redoLast()

    def sizeToolUp(self):
        try:
            self.active_tool.sizeUp()
        except AttributeError as e:
            print("Cannot resize active tool:", e)

    def sizeToolDown(self):
        try:
            self.active_tool.sizeDown()
        except AttributeError as e:
            print("Cannot resize active tool:", e)

    def changeColor(self, color):
        if self.active_tool:
            try:
                self.active_tool.setColor(color)
            except AttributeError as e:
                print('Cannot change color of active tool:', e)
        else:
            print('Press B to activate brush')

    def chooseTool(self, tool):
        self.active_tool = tool

    def resetTool(self):
        self.active_tool = None

if __name__ == "__main__":
    app = App()
    app.mainLoop()



