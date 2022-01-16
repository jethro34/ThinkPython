# create function mysqrt that takes a, chooses a reasonable value x, and returns an estimate of the square root of a

import math

def mysqrt(a):

    estimate = a / 2

    while True:
        # print("square root of:", a, "is (estimate)", estimate)
        better_estimate = (estimate + a/estimate) / 2
        if abs(better_estimate - estimate) < 0.0000001:
            # print("done. ", estimate, "is a value close enough to the square root of ", a)
            return better_estimate
            break
        estimate = better_estimate

def test_square_root():     # prints a test table
    if a == 1:
        print(" a,  mysqrt(a), math.sqrt(a), diff")
    print(a, mysqrt(a), math.sqrt(a), abs(mysqrt(a) - math.sqrt(a)))


for a in range(1, 10):
    test_square_root()
