# draws phrases

import turtle

coord_key = {'7': (-20, 40),  '8': (0, 40),  '9': (20, 40),
             '4': (-20, 0),   '5': (0, 0),   '6': (20, 0),
             '1': (-20, -40), '2': (0, -40), '3': (20, -40)}

alphabet = {'a': '1834', 'b': '76431', 'c': '943', 'd': '7614', 'e': '943045', 'g': '9435', 'i': '852', 'l': '7413',
            'n': '17863', 'o': '4862', 's': '8462', 't': '7890852', 'u': '729', 'v': '729', 'y': '759052', 'z': '7913',
            ' ': '10'}


def print_character(t, code, adjust, margin):
    t.penup()
    t.goto(margin + coord_key[code[0]][0] + adjust, coord_key[code[0]][1])  # setting initial position
    for ch in range(len(code[:-1])):
        if code[ch+1] == '0':
            continue
        elif code[ch] == '0':
            t.penup()
            t.goto(margin + coord_key[code[ch+1]][0] + adjust, coord_key[code[ch+1]][1])
        else:
            t.pendown()
            t.goto(margin + coord_key[code[ch+1]][0] + adjust, coord_key[code[ch+1]][1])
    t.penup()


def print_phrase(t, phrase, separation, margin):
    count = 0
    for ch in phrase:
        print_character(t, alphabet[ch], separation * count, margin)
        count += 1


pen = turtle.Turtle()
print(pen)

print_phrase(pen, "diaz canel singao", 60, -500)

pen.hideturtle()
turtle.mainloop()
             