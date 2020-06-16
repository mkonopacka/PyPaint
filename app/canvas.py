import pygame
import utils
import colors
from field import Field

class Canvas(Field):
    
    def __init__(self, app, width, height, bg_color = colors.WHITE, name = "canvas", lay_num = 3):
        super().__init__(app, width, height, bg_color, name)
        self.resetBackground(self.bg_color)
        self.ongoing = False
        self.active_tool = None
        self.temp = self.background.copy()
        self.temp.fill(colors.CLEAR)
        self.current = self.temp.copy()
        self.layers = [self.temp.copy() for _ in range(lay_num)]
        self.undone = []

    def display(self, dest, coords):
        # First blit background and current layer onto the display
        dest.blit(self.background, coords)
        dest.blit(self.current, coords)
        # Then active changes, if drawing on temporary layer
        if self.ongoing:
            dest.blit(self.temp, coords)

    # TODO pos should be relative
    def startDrawing(self, pos, tool):
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
        self.current.fill(colors.CLEAR)
        for layer in self.layers:
            self.current.blit(layer, (0,0))

    def undoLast(self):
        if len(self.undone) < len(self.layers):
            # move most recent layer from layers to undo stack
            self.undone.append(self.layers.pop())
            # add clear layer 0
            self.layers.insert(0, self.temp.copy())
            # update current
            self.currentUpdate()
            print("UNDONE")
        else:
            print("Can't undone more changes")

    def redoLast(self):
        if len(self.undone) > 0:
            del self.layers[0]
            self.layers.append(self.undone.pop())
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
        for layer in self.layers:
            layer.fill(colors.CLEAR)
        self.temp.fill(colors.CLEAR)
        self.resetBackground(colors.WHITE)

if __name__ == "__main__":
    pass
