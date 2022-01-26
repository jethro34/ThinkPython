def is_power(a, b):
    if a == b:
        return True
    return a % b == 0 and is_power(a / b, b)


print(is_power(2, 1))
