import abc as abc
import pygame
import pygame.freetype
import tool
import utils
import colors
from button import *
from field import Field
from math import floor

class Toolbar(Field):
    """
    Field subclass container for icons etc.; may contain sub-toolbars.

    Toolbar references the app instance in order to assign some app's methods to actions of icons
    stored by the toolbar. 
    icon.setAction() is called always inside Toolbar subclass. All toolbars 
    in the program are subclasses of Toolbar.
    """
    def_marg = 0.05
    def_color = colors.GREY

    def __init__(self, app, width, height, bg_color = def_color, name = "Toolbar", nrows = 4, ncols = 2):
        super().__init__(width, height, bg_color, name)
        self.app = app
        self.fillBackground(self.bg_color)
        self.nrows = nrows
        self.ncols = ncols
        self.max_icons = nrows * ncols

        # coordinates
        self.marg = int(Toolbar.def_marg * self.width)
        self.icon_w = int((self.width - (ncols + 1) * self.marg) // ncols)
        self.icon_h = int((self.height - (nrows + 1) * self.marg) // nrows)
        dx = self.icon_w + self.marg
        dy = self.icon_h + self.marg
        xs = [self.marg + k*dx for k in range(ncols)]
        ys = [self.marg + k*dy for k in range(nrows)]
        self.icons_coords = [(x,y) for x in xs for y in ys]

    @classmethod
    def setDefaultMargin(cls, marg):
        cls.def_marg = marg

    @classmethod
    def setDefaultColor(cls, col):
        cls.def_col = col

class ColorsBar(Toolbar):
    def __init__(self, app, width, height, bg_color = Toolbar.def_color, name = "Colors toolbar", nrows = 2, ncols = 4):
        super().__init__(app, width, height, bg_color, name, nrows, ncols)

        # Add ColorIcons
        cols = [colors.RED, colors.BLUE, colors.GREEN, colors.WHITE, colors.YELLOW, colors.BLACK, colors.NAVY, colors.ORANGE]
        icons = [ColorIcon(self.icon_w, col) for col in cols]
        for icon, coords in zip(icons, self.icons_coords):
            icon.setAction(self.app.changeColor, icon.color)
            self.addMember(icon, coords)

class MainToolbar(Toolbar):
    def __init__(self, app, width, height, bg_color = Toolbar.def_color, name = "Main toolbar", nrows = 4, ncols = 4):
            super().__init__(app, width, height, nrows = nrows, ncols = ncols, name = name)

            self.part_w = self.width  - self.marg
            self.part_h = self.height // self.nrows
            
            # Add colors toolbar
            colors = ColorsBar(app, self.part_w, self.part_h)
            self.addMember(colors, (self.marg, self.marg))

            # Add options toolbar
            bottom = Toolbar(app, self.part_w, self.part_h, name = "Options toolbar", nrows = 2, ncols = 4)
            self.addMember(bottom, (self.marg, self.height - self.part_h))

            undo_icon = ImageIcon(self.icon_w, 'images/undo.png', name = 'Undo icon')
            undo_icon.setAction(self.app.undo)
            bottom.addMember(undo_icon, bottom.icons_coords[0])
            
            redo_icon = ImageIcon(self.icon_w, 'images/redo.png', name = 'Redo icon')
            redo_icon.setAction(self.app.redo)
            bottom.addMember(redo_icon, bottom.icons_coords[1])

            plus_icon = ImageIcon(self.icon_w, 'images/plus.png', name = 'Plus icon')
            plus_icon.setAction(self.app.sizeToolUp)
            bottom.addMember(plus_icon, bottom.icons_coords[2])

            minus_icon = ImageIcon(self.icon_w, 'images/minus.png', name = 'Minus icon')
            minus_icon.setAction(self.app.sizeToolDown)
            bottom.addMember(minus_icon, bottom.icons_coords[3])

            brush_icon = ImageIcon(self.icon_w, 'images/brush.png', name = 'Brush icon')
            brush_icon.setAction(self.app.chooseTool, tool.brush1)
            bottom.addMember(brush_icon, bottom.icons_coords[4])