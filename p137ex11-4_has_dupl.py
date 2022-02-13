def has_duplicates(liste):
    """Checks for a duplicate item in a given list using a dictionary."""
    dikt = {}
    for item in liste:
        if item in dikt:
            return True
        dikt[item] = True
    return False


t = [1, 5, 23, 4, 7, 12, 4, 66]
if not has_duplicates(t):
    print("there ain't no duplicates")
else:
    print('there are duplicates')
