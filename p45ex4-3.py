import turtle
import math

def triangler(t, n, in_lngth):
    t.fd(in_lngth)
    t.lt(180 - 360 / (2 * n))
    t.fd(2 * in_lngth * math.sin(90 - 180 / n))
    t.lt(180 - 360 / (2 * n))
    t.fd(in_lngth)

def full_polygon(t, n, side_length):
    for i in range(n):
        t.fd(side_length)
        t.lt(360 / n)


bob = turtle.Turtle()
print(bob)

triangler(bob, 4, 100)

#bob.hideturtle()
turtle.mainloop()
