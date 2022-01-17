# draws a wheel graph given the number of sides and radius

import turtle
import math

def triangler(t, sides, radius):
    """Draws an internal triangle in the wheel"""
    side_angle = (sides - 2) * 90 / sides
    side_length = 2 * radius * math.sin(math.radians(180 / sides))

    t.fd(radius)
    t.lt(180 - side_angle)
    t.fd(side_length)
    t.lt(180 - side_angle)
    t.fd(radius)
    t.lt(180)

def wheeler(t, sides, radius):
    """Draws the wheel"""
    for i in range(sides):
        triangler(t, sides, radius)


bob = turtle.Turtle()
print(bob)

wheeler(bob, 3, 100)

bob.hideturtle()
turtle.mainloop()
