def create_list():
    """Creates a list by reading from a file."""
    w_list = []
    fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
    for line in fin:
        w_list.append(line.strip())
    return w_list


def in_bisect(l, target):
    """Returns True if target is in a given list, False otherwise, using bi-section."""
    mini = 0
    maxi = len(l) - 1
    if l[mini] <= target <= l[maxi]:
        while mini <= maxi:
            indeks = mini + (maxi - mini) // 2
            if l[indeks] == target:
                return True
            elif l[indeks] > target:
                maxi = indeks - 1
            else:
                mini = indeks + 1
    return False


def interlock(big_w):
    """Returns a tuple with three interlocked words from a given word."""
    w1 = big_w[::3]
    w2 = big_w[1::3]
    w3 = big_w[2::3]
    return w1, w2, w3


def check(l, w1, w2, w3):
    """Checks interlocks from a given word."""
    global hits, word

    if in_bisect(l, w1) and in_bisect(l, w2) and in_bisect(l, w3):
        print(word, w1, w2, w3)
        hits += 1


liste = create_list()
hits = 0

for word in liste:
    check(liste, interlock(word)[0], interlock(word)[1], interlock(word)[2])

print('there were', hits, 'hits!')
