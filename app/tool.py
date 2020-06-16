import pygame
import utils
import abc
import pygame.gfxdraw
from field import Field


class Tool(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod # TODO abstract property?
    def can_draw(self):
        pass

class Brush(Tool): 

    min_size = 1
    max_size = 50
    
    def __init__(self, color, size = 4, name = "new brush"):
        super().__init__(name)
        self.size = size
        self.color = color
        self.name = name
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
            print(f"This brush can't have size {size}")
    
    def startPainting(self, surface, pos):
        self.current_surface = surface
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
        print(f"Brush started painting on {surface}")

    def continuePainting(self, pos, rel):
        end = pos
        start = (pos[0] - rel[0], pos[1] - rel[1])
        pygame.draw.line(self.current_surface, self.color, start, end, 2 * self.size)
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
        print(f"Still painting on {self.current_surface}!")

    def endPainting(self, pos):
        pygame.draw.circle(self.current_surface, self.color, pos, self.size)
        print(f"Ended painting on {self.current_surface}")
    
    def getName(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def modifyCanvas(self, canvas, mousePos):
        pass


