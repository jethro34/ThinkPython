import math


class Point:
    """Creates a Point class"""

    def __init__(self, x, y):
        """something"""
        self.x = x
        self.y = y


class Circle:
    """Creates a Circle class"""

    def __init__(self, center, radius):
        """something"""
        self.center = center
        self.radius = radius


class Rectangle:
    """Creates a horizontal Rectangle class"""

    def __init__(self, c1, c3):
        self.c1 = c1
        self.c3 = c3


def dist_bw_points(pt1, pt2):
    return math.sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)


def point_in_circle(pt, cir):
    return dist_bw_points(cir.center, pt) <= cir.radius


def rect_in_circle(rect, cir):
    c2 = Point(rect.c3.x, rect.c1.y)
    c4 = Point(rect.c1.x, rect.c3.y)
    return (point_in_circle(rect.c1, cir) and point_in_circle(c2, cir) and
            point_in_circle(rect.c3, cir) and point_in_circle(c4, cir))


# pointx = Point(226, 100)
# print(point_in_circle(pointx, circl))


circl = Circle(Point(60, 65), 53)
box = Rectangle(Point(20, 30), Point(100, 100))

print(rect_in_circle(box, circl))
