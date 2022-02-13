def sumall(*args):
    """ Sums any number of numbers."""
    return sum(args)


def rec_sum(*args):
    """ Sums any number of numbers recursively."""
    if len(args) == 1:
        return int(args[0])
    return int(args[0]) + rec_sum(*args[1:])

print(sumall(1, 2, 3, 4))

# print(rec_sum(10, 23, 22))
# print(sum((1, 2, 3, 5)))      # as a tuple iterable
# print(sum([1, 2, 3, 5]))      # as a list iterable
