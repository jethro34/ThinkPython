#def(print_n(string, n):    # prints a string n times by recursion
#    if n <= 0:
#        return
#    print(string)
#    print_n(string, n - 1)
# the exercise asks the above recursive function to be changed into an iterative one:

def print_n(string, n):   # prints a string n times by iteration
    while n > 0:
        print(string)
        n -= 1


print_n("bitch", 3)
