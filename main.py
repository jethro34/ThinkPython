# recursion example

def iterative_factorial(number):
    temporal = 1
    for i in range(1, number + 1):
        temporal = temporal * i
    return temporal


def recursive_factorial(number):
    if number == 1:
        return 1
    return number * recursive_factorial(number - 1)



print(iterative_factorial(3))
print(recursive_factorial(3))

