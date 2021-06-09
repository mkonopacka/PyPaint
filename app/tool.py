import pygame
import utils
import abc
import pygame.gfxdraw
<<<<<<< HEAD
import colors
=======
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
from field import Field


class Tool(abc.ABC):
<<<<<<< HEAD
    """
    Abstract class representing any tool that can be used to interact with the canvas. 
    """
=======
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d

    def __init__(self, name):
        self.name = name

<<<<<<< HEAD
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
=======
    @abc.abstractmethod # TODO abstract property?
    def can_draw(self):
        pass

class Brush(Tool): 
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d

    min_size = 1
    max_size = 50
    
<<<<<<< HEAD
    def __init__(self, color, size = 4, name = "Brush"):
        super().__init__(name)
        self.size = size
        self.color = color
=======
    def __init__(self, color, size = 4, name = "new brush"):
        super().__init__(name)
        self.size = size
        self.color = color
        self.name = name
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
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
<<<<<<< HEAD
            print(f"Size {size} is not allowed for active brush")
=======
            print(f"This brush can't have size {size}")
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
    
    def startPainting(self, surface, pos):
        self.current_surface = surface
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
<<<<<<< HEAD
=======
        print(f"Brush started painting on {surface}")
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d

    def continuePainting(self, pos, rel):
        end = pos
        start = (pos[0] - rel[0], pos[1] - rel[1])
        pygame.draw.line(self.current_surface, self.color, start, end, 2 * self.size)
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
<<<<<<< HEAD

    def endPainting(self, pos):
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
=======
        print(f"Still painting on {self.current_surface}!")

    def endPainting(self, pos):
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
        print(f"Ended painting on {self.current_surface}")
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
    
    def getName(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

<<<<<<< HEAD
# brushes:
brush1 = Brush(colors.BLUE, size = 20)
=======
    def modifyCanvas(self, canvas, mousePos):
        pass

>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d

