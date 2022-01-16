import turtle
import math

def square(t, side_length):
  for i in range(4):
    t.fd(side_length)
    t.lt(90)


def polygon(t, n, side_length):
  for i in range(n):
    t.fd(side_length)
    t.lt(360 / n)


def circle(t, radius):
  polygon(t, 360, radius * math.pi / 180)


def arc(t, radius, angle):
  for i in range(angle):
    t.fd(radius * math.pi / 180)
    t.lt(1)


bob = turtle.Turtle()
print(bob)

# square(bob, 50)
# polygon(bob, 5, 50)
circle(bob, 10)
arc(bob, 12, 360)


turtle.mainloop()
