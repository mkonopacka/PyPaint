import abc as abc
import pygame as pg
from field import Field
import colors
import pygame.freetype
import utils

class Button(Field):
    
    def __init__(self, app, width, height, bg_color = colors.DARK_GREY, name = "button"):
        super().__init__(app, width, height, bg_color, name)
        self.clicked = False
        self.app = app
        self.bd_color = colors.BLACK
        self.bd_thickness = 5

    def display(self, dest, coords):
        dest.blit(self.background, coords)
        if self.clicked:
            print(f"Drawing boundary of {self}")
            pg.draw.rect(self.background, self.bd_color, self.background.get_bounding_rect(), self.bd_thickness)
           
        for m in self.members: 
            if m.isVisible():
                m.display(self.background, self.members[m])

    def setAction(self, action):
        self.action = action # lambda or regular function?
    
    def click(self):
        self.clicked = True
        if self.action:
            self.action()

    def unclick(self):
        self.clicked = False
        self.fillBackground()
        print("Unclick")

    def isClicked(self):
        return self.clicked
    
# TODO
class TextButton(Button):

    default_font = pg.freetype.SysFont('Comic Sans MS', 30)
    
    @classmethod
    def setDefaultFont(cls, font):
        cls.default_font = font
    
    def __init__(self, app, width, height, bg_color, name = "text button", text = "default button", font = default_font):
        super().__init__(app, width, height, bg_color, name)
        self.text = text
        self.font = font

    def setText(self, text):
        self.text = text

    def setFont(self, font):
        self.font = font

class Icon(Button):

    def __init__(self, app, size, bg_color = colors.BLACK, name = "icon", img_path = None):
        super().__init__(app, size, size, bg_color, name)
        if img_path:
            self.setImage(img_path)
        else:
            self.image = None

    def setImage(self, path):
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, self.size)
        self.background  = self.image

class ColorIcon(Icon):
    def __init__(self, app, size, color, name = "color icon"):
        super().__init__(app, size, color, name)
        self.color = color
        
        def tryChangeColor():
            try:
                self.app.active_tool.setColor(color)
            except AttributeError:
                print("Cannot set color of active tool")

        self.setAction(tryChangeColor)



