def pointInsideRect(point, corner, rwidth, rheight):
    
    types = [int, float]

    if not (type(point) == type(corner) == tuple):
        raise TypeError('first two arguments must be tuples.')

    if not (type(rwidth) in types and type(rheight) in types):
        raise TypeError('rwidth and rheight must be integers or floats.')

    if rwidth <= 0 or rheight <= 0:
        raise ValueError('rwidth and rheight must be positive.')

    for x in (point[0], point[1], corner[0], corner[1]):
        if not type(x) in types:
            raise TypeError('all coordinates must be integers or floats.')

        if x < 0:
            raise ValueError('all coordinates cannot be negative.')
    
    return corner[0] <= point[0] and corner[0] + rwidth >= point[0] and corner[1] <= point[1] and corner[1] + rheight >= point[1]

if __name__ == '__main__':
    x = (1, 1)
    y = (1, 10)
    a = 9
    b = 5
    print(pointInsideRect(x, y, a, b))
