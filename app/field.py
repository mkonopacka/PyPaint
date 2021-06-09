import abc as abc
import pygame as pg
import pygame.freetype
import utils
import colors

pg.freetype.init()

class Field():
    """
    Class representing rectangular elements on the screen (i.e. canvas, icons); may consist of subfields and serve as a container for them. 

    Attributes:

        name (string): name of the Field used for testing with __str__ representation.
        bg_color: tuple of 3 integers between 0 and 255 storing the RGB value of color of field's background
        width (int): rectangle's width
        height(int): rectangle's height
        members: dictionary storing subfields as keys and their coordinates relative to the field's top-left corner as values
        visible: boolean indicating whether the field should be visible
        backgroud: pygame Surface used to represent the field (transparent if bg_color alpha is 0)
    """

    def __init__(self, width, height, bg_color = colors.CLEAR, name = "Field"):

        self.name = name
        self.bg_color = bg_color
        self.resize(width, height)
        self.members = {}
        self.visible = True

    def getHovered(self, rel_mouse): # (0,0) = top-left corner of parent field
        """
        Recursively checks whether mouse is hovering over any of visible subfields based on relative position of the cursor 
        and subfield relative coordinates (if not, returns the main field).
        """
        for m in self.members:
            if m.isVisible():
                if utils.pointInsideRect(rel_mouse, self.members[m], m.width, m.height):
                    x = rel_mouse[0] - self.members[m][0]
                    y = rel_mouse[1] - self.members[m][1]
                    return m.getHovered((x,y))
        return self
    
    def display(self, dest, coords):
        """
        Blits (pygame.blit()) the field's background Surface onto surface passed as dest on position passed as coords;
        then recursively blits all visible subfields onto itself.
        """
        if self.isVisible:
            dest.blit(self.background, coords)
            for m in self.members: 
                if m.isVisible():
                    m.display(self.background, self.members[m])

    def hide(self):
        """
        Sets field.visible to False.
        """
        self.visible = False

    def unhide(self):
        self.visible = True

    def addMember(self, member, coords):
        """
        Adds a new subfield at the given position.
        """
        self.members[member] = coords

    def removeMember(self, member):
        """
        Removes chosen subfield from members dict.
        """
        self.members.pop([member])

    def replaceMember(self, member):
        coords = self.members.pop(member)
        self.addMember(member, coords)
    
    def moveMember(self, member, dx, dy):
        """
        Changes coordinates of chosen subfield by adding (dx,dy)
        """
        self.members[member][0] += dx
        self.members[member][1] += dy

    def __str__(self):
        """
        Returns name of the field.
        """
        return f"{self.name}"

    def fillBackground(self, color = None):
        """
        If color is specified always sets it as the new field.bg_color and refills the background surface; otherwise if the field
        has an image, refills background with the image and if not, refills background with current bg_color.
        """
        if color:
            self.bg_color = color

        elif hasattr(self, 'image') and self.image:
            self.background.blit(self.image, (0,0))
            return

        self.background.fill(self.bg_color)

    def resize(self, width, height):
        """
        Sets newly created Surface with specified width and height as a background and then calls fillBackground() method.
        """
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.background = pg.Surface(self.size, pg.HWSURFACE|pg.DOUBLEBUF).convert_alpha()
        self.fillBackground()
        
    def resizeBy(self, percent):
        """
        The same as resize(), but scales the Surface by some percent (both width and height)
        """
        if percent <= 0:
            raise ValueError('resizeBy accepts only positive values as an argument')
        else:
            w = int(self.width*float)
            h = int(self.height*float)
            self.resize(w, h)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSize(self):
        return self.size

    def isVisible(self):
        return self.visible

class MainView(Field):
    """
    The Field used to recursively access canvas and toolbar as subfields from program's main loop.
    """
    
    def __init__(self, width, height, canvas, toolbar, name = "MainView"): 
        super().__init__(width, height, name = name)
        self.addMember(canvas, (0,0))
        self.addMember(toolbar, (canvas.width, 0))


if __name__ == '__main__':
    print(help(Field))
