

def recurse(n, s):
    """Finds out the sum of values from 0 up to a positive integer n, including a base value s"""
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)