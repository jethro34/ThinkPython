# draws alphabet letters

import turtle

def rotate(t, orig_coord, dest_coord):
    return


def print_letter(t, string_code):
    pointer.goto(coordinates(string_code[1]))                            # setting pen's initial location 
    for ch in string_code[:-1]:
        if ch == '0' or string_code[ch+1] == '0':
            continue
        t.pendown()
        #rotate(coordinates(ch), coordinates(string_code[ch+1]))
        #draw_line(coordinates(ch), coordingates(string_code[ch+1]))
    #pen.up


def something():
    return


pointer = turtle.Turtle()
print(pointer)
print_letter("1834")

        
        
