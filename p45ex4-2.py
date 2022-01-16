# draws a flower with optional overlapped petals

import turtle
import math

def arc(t, radius, angle):
  for i in range(angle):
    t.fd(radius * math.pi / 180)
    t.lt(1)

def draw_petal(radius, angle):
    arc(bob, radius, angle)
    bob.lt(180 - angle)
    arc(bob, radius, angle)
    bob.lt(180)

def draw_flower(radius, angle, overlap=False):
    """Draws a flower with optional overlapped petals"""

    for i in range(360 // angle):
        draw_petal(radius, angle)
    if overlap:
        bob.lt(angle // 2)
        draw_flower(radius, angle)

    
bob = turtle.Turtle()
print(bob)

draw_flower(500, 15)

turtle.mainloop()
