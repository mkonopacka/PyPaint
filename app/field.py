import abc as abc
import pygame as pg
import pygame.freetype
import utils
import colors

pg.freetype.init()

class Field(abc.ABC):

    def __init__(self, app, width, height, bg_color = colors.CLEAR, name = "default field name"):

        self.app = app
        self.name = name
        self.bg_color = bg_color
        self.resize(width, height)
        self.members = {}
        self.visible = True

    @abc.abstractmethod
    def click(self):
        pass

    @abc.abstractmethod
    def unclick(self):
        pass
    
    def getHovered(self, rel_mouse): # uses coords with (0,0) at top left corner of self
        for m in self.members:
            if m.isVisible():
                if utils.pointInsideRect(rel_mouse, self.members[m], m.width, m.height):
                    # calculate new relative position of mouse (now: top left corner + new_pos = rel_mouse)
                    x = rel_mouse[0] - self.members[m][0]
                    y = rel_mouse[1] - self.members[m][1]
                    return m.getHovered((x,y))
        return self
    
    def display(self, dest, coords):  # recursively display all subfields (members)
        if self.isVisible:
            dest.blit(self.background, coords)
            for m in self.members: 
                if m.isVisible():
                    m.display(self.background, self.members[m])
        

    def isVisible(self):
        return self.visible

    def hide(self):
        self.visible = False

    def unhide(self):
        self.visible = True

    def addMember(self, member, coords):
        self.members[member] = coords

    def removeMember(self, member):
        del self.members[member]

    def replaceMember(self, member):
        coords = self.members.pop(member)
        self.addMember(member, coords)
    
    def moveMember(self, member, dx, dy):
        self.members[member][0] += dx
        self.members[member][1] += dy

    def __str__(self):
        return f"{self.name}"

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSize(self):
        return self.size

    def fillBackground(self, color = None):
        
        print(f"fillBackground called on {self}")
        if color:
            self.bg_color = color

        elif hasattr(self, 'image') and self.image:
            self.background = self.image
            print("Setting image as a background")
            return

        self.background.fill(self.bg_color)

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.background = pg.Surface(self.size, pg.HWSURFACE|pg.DOUBLEBUF).convert_alpha()
        self.fillBackground()
        
    def resizeBy(self, float):
        w = int(self.width*float)
        h = int(self.height*float)
        self.resize(w, h)



