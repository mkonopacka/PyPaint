import abc as abc
import pygame as pg
from field import Field
import colors
import pygame.freetype
import utils

class Button(Field):
<<<<<<< HEAD
    """
    Parent class to all icons and other clickable, rectangular objects. Subclass of Field class.

    Attributes (for other attributes see Field):
        is_pressed (bool)
        bd_color: color of the border visible when the button is pressed in RGB format
        bd_thickness: thickness of the border visible when the button is pressed
        action: reference to the function called when clicked
        action_args: non-keyword arguments passed to the function assigned to action attribute
        action_kwargs: keyword argument passed to the function assigned to action attribute

    """
    
    def_bd_color = colors.BLACK
    def_bd_thickness = 5
    
    def __init__(self, width, height, bg_color = colors.DARK_GREY, name = "Button", bd_color = def_bd_color, bd_thickness = def_bd_thickness):
        super().__init__(width, height, bg_color, name)
        self.is_pressed = False
        self.bd_color = bd_color
        self.bd_thickness = bd_thickness
    
    def setAction(self, func, *args, **kwargs):
        """
        Assigns given function to the action attribute and it's arguments to action_args and action_kwargs.
        """
        self.action = func
        self.action_args = args
        self.action_kwargs = kwargs

    def click(self):
        """
        Sets is_pressed attribute to True, draws border of the button and tries to run action assigned to the button.
        """
        self.is_pressed = True
        pg.draw.rect(self.background, self.bd_color, self.background.get_bounding_rect(), self.bd_thickness)
           
        if hasattr(self, 'action') and self.action:
            self.action(*self.action_args, **self.action_kwargs)
        else:
            print('No action available')

    def unclick(self):
        """
        Sets is_pressed to False and calls fillBackground() method.
        """
        self.is_pressed = False
        self.fillBackground()
    
# TODO
# class TextButton(Button):

#     default_font = pg.freetype.SysFont('Verdana', 30)
    
#     @classmethod
#     def setDefaultFont(cls, font):
#         cls.default_font = font
    
#     def __init__(self, width, height, bg_color, name = "TextButton", text = "Some text", font = default_font):
#         super().__init__(width, height, bg_color, name)
#         self.text = text
#         self.font = font

#     def setText(self, text):
#         self.text = text

#     def setFont(self, font):
#         self.font = font

class Icon(Button, abc.ABC):
    """
    Subclass of Button to represent square button.
    """

    def __init__(self, size, bg_color = colors.BLACK, name = "Icon"):
        super().__init__(size, size, bg_color, name)

class ImageIcon(Icon):
    """
    Subclass of Icon with image attribute.
    """

    def __init__(self, size, img_path, bg_color = colors.BLACK, name = "ImageIcon"):
        super().__init__(size, bg_color, name)
        self.setImage(img_path)

    def setImage(self, path):
        """
        Loads image with help of pygame functions, resizes it to fit the icon and sets as it's image attribute. 
        """
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, self.size)
        self.background  = self.image.copy()

class ColorIcon(Icon):
    """
    Subclass of Icon with solid color instead of image.
    """
    def __init__(self, size, color, name = "ColorIcon"):
        super().__init__(size, color, name)
        self.color = color
=======
    
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
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d



