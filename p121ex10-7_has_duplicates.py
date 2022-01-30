def has_duplicates(list1):
    """Checks for a duplicate item in a given list."""
    for index1 in range(len(list1)):
        for index2 in range(index1 + 1, len(list1)):
            if list1[index1] == list1[index2]:
                return True
    return False


t = [1, 4, 5, 12, 23, 4]
print(has_duplicates(t))
