import abc as abc
import pygame
import pygame.freetype
import utils
import colors
from button import *
from field import Field
from math import floor

# # component of a toolbar
# class Row(Field):
    
#     def __init__(self, app, width, height, name, ncols):
#         super().__init__(app, width, height, name = "row")
#         self.ncols = ncols

#     def click(self):
#         pass

#     def unclick(self):
#         pass


class Toolbar(Field):
    
    def_marg = 0.05
    def_color = colors.GREY
    def_bd_color = colors.DARK_GREY
    def_bd_th = 5

    def __init__(self, app, width, height, bg_color = def_color, name = "toolbar", nrows = 4, ncols = 2, bd_color = def_bd_color, bd_thickness = def_bd_th):
        super().__init__(app, width, height, bg_color, name)
        self.resetBackground(self.bg_color)
        self.bd_color = bd_color
        self.bd_thickness = bd_thickness
        self.visible_borders = False
        self.max_icons = nrows * ncols

        # generate coords:
        self.marg = int(Toolbar.def_marg * self.width)
        self.icon_w = int((self.width - (ncols + 1) * self.marg) // ncols)
        self.icon_h = int((self.height - (nrows + 1) * self.marg) // nrows)
        dx = self.icon_w + self.marg
        dy = self.icon_h + self.marg
        xs = [self.marg + k*dx for k in range(ncols)]
        ys = [self.marg + k*dy for k in range(nrows)]
        self.icons_coords = [(x,y) for x in xs for y in ys]

    def click(self):
        print(f"Clicked f{self.name}")

    def unclick(self):
        pass

    def display(self, dest, coords):
        dest.blit(self.background, coords)
        if self.visible_borders:
            pg.draw.rect(self.background, self.bd_color, self.background.get_bounding_rect(), self.bd_thickness)
        for m in self.members: 
            if m.isVisible():
                m.display(self.background, self.members[m])

class ColorsBar(Toolbar):

    def __init__(self, app, width, height, bg_color = Toolbar.def_color, name = "colors bar", nrows = 2, ncols = 4):
        super().__init__(app, width, height, bg_color, name, nrows, ncols)

        # Add ColorIcons, by default 8 icons
        cols = [colors.RED, colors.BLUE, colors.GREEN, colors.WHITE, colors.YELLOW, colors.BLACK, colors.NAVY, colors.ORANGE]
        icons = [ColorIcon(self.app, self.icon_w, col) for col in cols]
        for icon, coords in zip(icons, self.icons_coords):
            self.addMember(icon, coords)

class MainToolbar(Toolbar):

    def __init__(self, app, width, height, bg_color = Toolbar.def_color, name = "main toolbar", nrows = 2, ncols = 4):
            super().__init__(app, width, height, nrows = nrows, ncols = ncols, name = name)
            self.visible_borders = False
            
            colors = ColorsBar(app, width  - 2, height // 4)
            self.addMember(colors, (2,2))


    def click(self):
        pass