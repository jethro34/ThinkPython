
d1 = {'a': 23, 'b': 12, 'c': 15, 'd': 20, 'e': 40, 'f': 9}
s1 = {'a', 'e', 'i', 'o', 'u'}


def subtract_set_from_dict(dikt, sett):
    """ Subtracts a set from a dictionary using set subtraction.
        Output: set """

    return set(dikt.keys()) - sett


print(subtract_set_from_dict(d1, s1))
