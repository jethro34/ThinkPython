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
        while mini <= maxi:
            index = mini + (maxi - mini) // 2
            if l[index] == target:
                return index
            elif l[index] > target:
                maxi = index - 1
            else:
                mini = index + 1
    return 'not in range'


def is_reverse(l):
    """Looks for reverse pairs in a given list and returns them in a list."""

    rev_list = []

    for i in range(len(l)):
        if in_bisect(l, l[i][::-1]) != 'not in range':
            rev_list.append((l[i], l[i][::-1]))
    return rev_list


t = ['baa', 'cab', 'cut', 'deaf', 'eez', 'tuc', 'zee']
print(t)
#print('the reverse pairs in list t are:')
#print(i for i in is_reverse(t))
print(in_bisect(t, t[6][::-1]))
