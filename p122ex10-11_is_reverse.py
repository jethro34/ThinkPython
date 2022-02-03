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
        index = in_bisect(l, l[i][::-1])
        if index != 'not in range' and index != i:
            rev_list.append((l[i], l[i][::-1]))
    return rev_list


t = created_list()
print('the reverse pairs in list t are:')
reverse_pairs = is_reverse(t)
for pair in reverse_pairs:
    print(pair)
