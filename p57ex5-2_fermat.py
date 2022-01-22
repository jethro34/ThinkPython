
def check_fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** n == c ** n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
        

def fermat_in():
    a = int(input("Enter value 'a': "))
    b = int(input("Enter value 'b': "))
    c = int(input("Enter value 'c': "))
    n = int(input("Enter value 'n': "))
    check_fermat(a, b, c, n)


fermat_in()
