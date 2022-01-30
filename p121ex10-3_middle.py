def middle(list1):
    """Returns all but first and last elements of a given list."""
    if len(list1) == 1:
        return []
    del list1[::len(list1) - 1]
    return list1


t = [1, 2, 9]
print(middle(t))
