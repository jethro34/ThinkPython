def is_sorted(list1):
    """Returns True if a given list is sorted."""
    return list1 == sorted(list1)


print(is_sorted([1, 3, 5]))
print(is_sorted(['b', 'a']))
