import pygame
import utils
import abc
import pygame.gfxdraw
import colors
from field import Field


class Tool(abc.ABC):
    """
    Abstract class representing any tool that can be used to interact with the canvas. 
    """
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def can_draw(self): # returns bool
        """
        Should return True for tools like a brush and False for tools like a probe.
        """
        pass

class Brush(Tool): 
    """
    Basic subtype of Tool; draws by blitting filled circles onto surface at given position.
    """
    min_size = 1
    max_size = 50
    
    def __init__(self, color, size = 4, name = "Brush"):
        super().__init__(name)
        self.size = size
        self.color = color
        self.current_surface = None

    def can_draw(self):
        return True

    def sizeUp(self):
        if self.size < Brush.max_size:
            self.size += 1
            print(f"Brush size: {self.size}")
        else:
            print("Bigger brush not allowed")

    def sizeDown(self):
        if self.size > Brush.min_size:
            self.size -= 1
            print(f"Brush size: {self.size}")
        else:
            print("Smaller brush not allowed")

    def setSize(self, size):
        if size <= Brush.max_size and size >= Brush.min_size:
            self.size = size
            print(f"Brush size: {self.size}")
        else:
            print(f"Size {size} is not allowed for active brush")
    
    def startPainting(self, surface, pos):
        self.current_surface = surface
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)

    def continuePainting(self, pos, rel):
        end = pos
        start = (pos[0] - rel[0], pos[1] - rel[1])
        pygame.draw.line(self.current_surface, self.color, start, end, 2 * self.size)
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)

    def endPainting(self, pos):
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
    
    def getName(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

# brushes:
brush1 = Brush(colors.BLUE, size = 20)

