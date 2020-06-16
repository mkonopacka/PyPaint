import pygame
import utils
from canvas import *
from toolbar import *
import colors
from field import Field

class MainView(Field):
    
    def __init__(self, app, width, height, canvas_width, name = "main view"): 
        super().__init__(app, width, height, name = name)
        canvas = Canvas(app, canvas_width, height)
        mainToolbar = MainToolbar(app, width - canvas_width, height)
        self.addMember(canvas, (0,0))
        self.addMember(mainToolbar, (canvas.getWidth(), 0))

    def click(self):
        pass

    def unclick(self):
        pass