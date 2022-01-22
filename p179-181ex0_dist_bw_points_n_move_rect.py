import math


class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    """Represents a rectangle. Attributes: width, height, corner."""


def dist_bw_points(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def move_rectangle(rect, xd, xy):
    rect.corner.x += xd
    rect.corner.y += xy


coord1 = Point(2, 3)
coord2 = Point(4, 2)

#print(dist_bw_points(coord1, coord2))

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point(0.0, 0.0)

move_rectangle(box, 5, 8)
print("The rectangle's corner is at: " + str(box.corner.x) + ":" + str(box.corner.y))
