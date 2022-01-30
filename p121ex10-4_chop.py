def chop(list1):
    """Removes first and last items from a given list while returning None."""
    if len(list1) == 1:
        del list1[0]
        return None
    del list1[0::len(list1) - 1]
    return None


t = [1, 2, 3, 4, 5]
chop(t)
print(t)
