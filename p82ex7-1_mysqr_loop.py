# create function mysqrt that takes 'a', chooses a reasonable value x, and returns an estimate of the square root of 'a'

import math


def mysqrt(a):
    """Finds an estimate of the square root of """
    estimate = a / 2
    while True:
        better_estimate = (estimate + a/estimate) / 2
        if abs(better_estimate - estimate) < 0.0000001:
            return better_estimate
        estimate = better_estimate


def fill_in(blanks):
    for ch in range(13 - len(str(blanks))):
        print(" ", end="")


def test_square_root():
    """Prints a test table"""
    if num == 1:
        print("a   mysqrt(a)    math.sqrt(a) diff")
        print("-   ---------    ------------ ----")
    print(num, " ", round(mysqrt(num), 10), end="")
    fill_in(round(mysqrt(num), 10))
    print(round(math.sqrt(num), 10), end="")
    fill_in(round(math.sqrt(num), 10))
    print(abs(mysqrt(num) - math.sqrt(num)))


for num in range(1, 10):
    test_square_root()
