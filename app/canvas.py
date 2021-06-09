import pygame
import utils
import colors
from field import Field

class Canvas(Field):
<<<<<<< HEAD
    """
    Subclass of Field used to represent the drawing area of the screen.

    The implementation makes it possible to undo (or redo) changes in the following way: 
    Canvas consists of a few Surfaces (layers) each of which is originally transparent (it's bg_color is CLEAR).
    They are stored in layers list (used as a stack) except for two special layers named temp and current.
    Current is the layer blitted onto the background and composed of all layers in layers list. It is updated
    only when user ends to draw something new and releases the mouse. The temp layer is the one affected by drawing
    and displayed over the current during drawing. 
    When user ends drawing, layers are shifted down, which means that the one closest to the background is permamently blitted onto it and removed from the list, new clear temp is created
    and finally the current is updated. In order to undo changes layers are "shifted up" and the newest layer
    goes into undone list from which it can be restored in order to redo changes.

    Attributes (for other attributes see Field):
        ongoing: boolean value indicating whether drawing is ongoing
        active_tool: reference to the tool currently affecting the canvas
        temp: temporary drawing Surface
        current: see the description
        layers: list of layers
        undone: list of undone layers
    """
    
    def __init__(self, width, height, bg_color = colors.WHITE, name = "Canvas", lay_num = 3):
        super().__init__(width, height, bg_color, name)
=======
    
    def __init__(self, app, width, height, bg_color = colors.WHITE, name = "canvas", lay_num = 3):
        super().__init__(app, width, height, bg_color, name)
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
        self.fillBackground(self.bg_color)
        self.ongoing = False
        self.active_tool = None
        self.temp = self.background.copy()
        self.temp.fill(colors.CLEAR)
        self.current = self.temp.copy()
        self.layers = [self.temp.copy() for _ in range(lay_num)]
        self.undone = []

    def display(self, dest, coords):
<<<<<<< HEAD
        """
        See class description.
        """
        dest.blit(self.background, coords)
        dest.blit(self.current, coords)
=======
        # First blit background and current layer onto the display
        dest.blit(self.background, coords)
        dest.blit(self.current, coords)
        # Then active changes, if drawing on temporary layer
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
        if self.ongoing:
            dest.blit(self.temp, coords)

    # TODO pos should be relative
    def startDrawing(self, pos, tool):
<<<<<<< HEAD
        """
        Sets ongoing attribute to True and calls startPainting() method of given tool.
        """
        self.active_tool = tool
        self.ongoing = True
        self.active_tool.startPainting(self.temp, pos)

    def updateDrawing(self, pos, rel):
        """
        pos and rel are mouse_get_pos() attributes
        """
        self.active_tool.continuePainting(pos, rel)

    def endDrawing(self, pos):
        """
        Sets ongoing to False, calls endPainting() method of the tool, then calls shiftLayersDown() and empties undone list.
        """
        self.ongoing = False
        self.active_tool.endPainting(pos)
        Canvas.shiftLayersDown(self)
        self.resetUndone()

    def shiftLayersDown(self):
        self.background.blit(self.layers[0], (0,0))
        del self.layers[0]
        self.layers.append(self.temp.copy())
        self.temp.fill(colors.CLEAR)
        self.updateCurrent()

    def updateCurrent(self):
        """
        Refills the current layer with CLEAR color and then blits all layers onto it.
        """
=======
        self.active_tool = tool
        self.ongoing = True
        print(f"Start drawing, tool: {self.active_tool}")
        self.active_tool.startPainting(self.temp, pos)

    def updateDrawing(self, pos, rel):
        print("Updated drawing")
        self.active_tool.continuePainting(pos, rel)

    def endDrawing(self, pos):
        self.ongoing = False
        print("Ended drawing")
        self.active_tool.endPainting(pos)
        Canvas.shiftLayersDown(self)

    def shiftLayersDown(self):
        # from layer 0 onto background = can't undo this layer anymore
        self.background.blit(self.layers[0], (0,0))
        # then shift all layers towards layer 0: remove layer 0 and push temp onto layers stack and create new clear temp
        del self.layers[0]
        self.layers.append(self.temp.copy())
        self.temp.fill(colors.CLEAR)
        # now blit state of layers onto self.current from 0 to n-1 (closest to temp)
        self.currentUpdate()

    def currentUpdate(self):
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
        self.current.fill(colors.CLEAR)
        for layer in self.layers:
            self.current.blit(layer, (0,0))

    def undoLast(self):
        if len(self.undone) < len(self.layers):
<<<<<<< HEAD
            self.undone.append(self.layers.pop())
            self.layers.insert(0, self.temp.copy())
            self.updateCurrent()
        else:
            print("Can't undo more changes")
=======
            # move most recent layer from layers to undo stack
            self.undone.append(self.layers.pop())
            # add clear layer 0
            self.layers.insert(0, self.temp.copy())
            # update current
            self.currentUpdate()
            print("UNDONE")
        else:
            print("Can't undone more changes")
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d

    def redoLast(self):
        if len(self.undone) > 0:
            del self.layers[0]
            self.layers.append(self.undone.pop())
<<<<<<< HEAD
            self.updateCurrent()
        else:
            print("Can't redo more changes")

    def reset(self):
        """
        Clears the canvas and undone list.
        """
=======
            self.currentUpdate()
            print("REDONE")
        else:
            print("Can't redo anything more")

    def click(self):
        pass

    def unclick(self):
        pass

    def hide(self):
        pass

    def reset(self):
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d
        for layer in self.layers:
            layer.fill(colors.CLEAR)
        self.temp.fill(colors.CLEAR)
        self.fillBackground(colors.WHITE)
<<<<<<< HEAD
        self.resetUndone()

    def resetUndone(self):
        self.undone = []

    def getCurrent(self):
        """
        Returns Surface object representing the current state of the canvas.
        """
        img = self.background.copy()
        img.blit(self.current, (0,0))
        return img
=======
>>>>>>> cfade769e8cb13a6cf0c18c7248246e8cebe9d1d

if __name__ == "__main__":
    pass
