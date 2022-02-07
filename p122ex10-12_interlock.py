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
            indeks = mini + (maxi - mini) // 2
            if l[indeks] == target:
                return indeks
            elif l[indeks] > target:
                maxi = indeks - 1
            else:
                mini = indeks + 1
    return 'not in range'


def interlocks(w1, w2):
    """Returns a tuple with interlocks from two given words."""
    temp = ''
    temp_rev = ''
    for ch1, ch2 in zip(w1, w2):
        temp += ch1 + ch2
        temp_rev += ch2 + ch1
    return temp, temp_rev


def find_w2_n_check(l, w1):
    """Checks interlocks from a given word and the next same-length word in a given list."""
    global hits
    for w2_indeks in range(l.index(w1), len(l)):
        if len(w1) == len(l[w2_indeks]):
            if in_bisect(l, interlocks(w1, l[w2_indeks])[0]) != 'not in range':
                print(w1, l[w2_indeks], l[in_bisect(l, interlocks(w1, l[w2_indeks])[0])])
                hits += 1
            elif in_bisect(l, interlocks(w1, l[w2_indeks])[1]) != 'not in range':
                print(w1, l[w2_indeks], l[in_bisect(l, interlocks(w1, l[w2_indeks])[1])])
                hits += 1


liste = created_list()
hits = 0

for word in liste:
    if len(word) < 4:
        find_w2_n_check(liste, word)

print('there were', hits, 'hits!')
