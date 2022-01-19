# draws alphabet letters

import turtle

def rotate_n_draw(t, orig_coord, dest_coord):
    to_angle = t.towards(dest_coord)
    t.setheading(to_angle)
    distance = math.sqrt((dest_coord[1] - orig_coord[1]) ** 2 + (dest_coord[0] - orig_coord[0]) ** 2)
    t.forward(distance)
    return


def print_letter(t, string_code):
    pointer.goto(coordinates(string_code[0]))         # setting pen's initial location 
    for ch in string_code[:-1]:
        if ch == '0' or string_code[ch+1] == '0':
            continue
        t.pendown()
        rotate_n_draw(t, coordinates(ch), coordinates(string_code[ch+1]))
    t.penup()


def something():
    return


pointer = turtle.Turtle()
print(pointer)
print_letter(pointer, "1834")

        
        
