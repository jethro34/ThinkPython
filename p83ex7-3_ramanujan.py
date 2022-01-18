# computes and returns an estimate of pi using the Ramanujan series

import math


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def compare_w_pi(step, num):
    if step == 0:
        print("step  Python pi:          Ramanujan pi:         diff:")
    print(step, "   ", math.pi, " ", num, "   ", abs(num - math.pi))


def estimate_pi():
    """Computes and returns successive estimates of pi using the Ramanujan series"""
    k = 0
    summation = 0
    while True:
        term = factorial(4 * k) * (1103 + 26390 * k) / (factorial(k) ** 4 * 396 ** (4 * k))
        summation += term
        temp_pi = 1 / (2 * math.sqrt(2) / 9801 * summation)
        compare_w_pi(k, temp_pi)
        if term < 1e-15:
            return temp_pi
        else:
            k += 1


estimate_pi()
