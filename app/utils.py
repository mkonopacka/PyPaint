
def pointInsideRect(point, corner, rwidth, rheight):
    return corner[0] <= point[0] and corner[0] + rwidth >= point[0] and corner[1] <= point[1] and corner[1] + rheight >= point[1]
