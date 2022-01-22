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


def dist_bw_points(pt1, pt2):
    return math.sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)


def point_in_circle(cir, pt):
    return dist_bw_points(cir.center, pt) <= cir.radius


circle = Circle((150, 100), 75)
pointx = Point(75, 100)

print(point_in_circle(circle, pointx))
