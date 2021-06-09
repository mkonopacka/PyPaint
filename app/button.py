import abc as abc
import pygame as pg
from field import Field
import colors
import pygame.freetype
import utils

class Button(Field):
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



