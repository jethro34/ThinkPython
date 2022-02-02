def created_list():
    """Creates a list by reading from a file."""
    w_list = []
    fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
    for line in fin:
        w_list.append(line.strip())
    return w_list


def in_bisect(l, target):
    """Returns the index of target in a given list l, using bi-section."""
    mini = 0
    maxi = len(l) - 1
    if l[mini] <= target <= l[maxi]:
        while True:
            index = mini + (maxi - mini) // 2
            if l[index] == target:
                return index
            elif l[index] > target:
                maxi = index - 1
            else:
                mini = index + 1
    return 'not in range'


print(in_bisect(created_list(), 'aha'))
