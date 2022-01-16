# prints a square grid

def horiz(corners_num, corner_char, inner_length, inner_char=" "):
    for i in range(1, corners_num):
        print(corner_char, end="")
        for j in range(1, inner_length):
            print(inner_char, end="")
    print(corner_char)


def vert(func, corners_num, corner_char, edge_char, inner_length, inner_char):
    for i in range(1, corners_num):
        func(corners_num, corner_char, inner_length, inner_char)
        for j in range(1, corners_num):
            func(corners_num, edge_char, inner_length)
    func(corners_num, corner_char, inner_length, inner_char)


vert(horiz, 4, "+", "|", 10, "-")
