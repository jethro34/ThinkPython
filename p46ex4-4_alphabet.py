# draws alphabet letters

import turtle
import math

coord_key = {'1': (-10, -20), '2': (0, -20), '3': (10, -20), '4': (-10, 0),
             '5': (0, 0), '6': (10, 0), '7': (-10, 20), '8': (0, 20), '9': (10, 20)}

def rotate_n_draw(t, orig_coord, dest_coord):
    to_angle = t.towards(dest_coord)
    t.setheading(to_angle)
    distance = math.sqrt((dest_coord[1] - orig_coord[1]) ** 2 + (dest_coord[0] - orig_coord[0]) ** 2)
    t.forward(distance)


def print_letter(t, string_code):
    pointer.goto(coord_key[string_code[0]])         # setting pen's initial location
    count = 0 
    for ch in string_code[:-1]:
        count += 1
        if ch == '0' or string_code[count] == '0':
            continue
        t.pendown()
        rotate_n_draw(t, coord_key[ch], coord_key[string_code[count]])
    t.penup()


pointer = turtle.Turtle()
#print(pointer)
print_letter(pointer, "1834")
pointer.hideturtle()
