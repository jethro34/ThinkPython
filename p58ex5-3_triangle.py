

def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    else:
        print("Yes")


def triangle_in():
    a = int(input("Enter side 'a': "))
    b = int(input("Enter side 'b': "))
    c = int(input("Enter side 'c': "))
    is_triangle(a, b, c)


triangle_in()

