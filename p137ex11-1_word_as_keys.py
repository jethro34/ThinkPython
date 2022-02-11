def create_list():
    """Creates a list by reading from a file."""
    w_list = []
    fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
    for line in fin:
        w_list.append(line.strip())
    return w_list


def w2dikt(liste):
    """Reads and stores words as keys in a dictionary."""
    dikt = {}
    for word in liste:
        dikt[word] = ''
    return dikt


def in_bisect(l, target):
    """Returns True if there is a target in list l, using bi-section."""
    mini = 0
    maxi = len(l) - 1
    while l[mini] <= target <= l[maxi]:
        index = mini + (maxi - mini) // 2
        if l[index] == target:
            return True
        elif l[index] > target:
            maxi = index - 1
        else:
            mini = index + 1
    return False


def is_in_dikt(d, target):
    """Returns True if target is a key in dictionary d."""
    return target in d


liste = create_list()
dikt = w2dikt(liste)

print('list search:', in_bisect(liste, 'ahchoo'))
print('dictionary search:', is_in_dikt(dikt, 'ahchoo'))
