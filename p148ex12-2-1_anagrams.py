def alpha_skeleton(wort):
    """ Takes in a word and returns its letters sorted.
        Output: tuple """

    return tuple(sorted(wort))


def dict_from_file():
    """ Reads words from a file and creates a dictionary whose keys are forming letters and values words.
        Output: dictionary of the type (tuple): [list] """

    dikt = {}
    fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
    for line in fin:
        w1 = line.strip()
        w2 = alpha_skeleton(w1)
        dikt.setdefault(w2, []).append(w1)
    return dikt


def anagram_dict(dikt):
    """ Takes in a dictionary and creates another whose keys are forming letters and values anagrams.
        Output: dictionary of the type (tuple): [list] """

    dikt2 = {}
    for tupel in dikt:
        if len(dikt[tupel]) == 1:
            continue
        else:
            dikt2[tupel] = dikt[tupel]
    return dikt2


def sort_freq(dikt):
    """ Takes in a forming-letters-to-word dictionary and turns out a frequency-organized list.
        Output: list of tuples """

    l1 = []
    for item in dikt:
        l1.append(tuple(dikt[item]))
    return sorted(l1, key=len, reverse=True)


def letter_set(dikt):
    """ Takes in a forming-letters to anagrams dictionary and creates another with 8-letter sets to number of anagrams.
        Output: dictionary of the type (tuple) : integer """

    dikt3 = {}
    for tupel in dikt:
        if len(set(tupel)) == 8:
            dikt3[tuple(sorted(set(tupel)))] = dikt3.setdefault(tuple(sorted(set(tupel))), 0) + 1
    return dikt3


anagrams = anagram_dict(dict_from_file())

# 12-2-1 anagrams
#for item in anagrams:
#   print(item, anagrams[item])

# 12-2-2 frequency
#for item in sort_freq(anagram_dict(dict_from_file())):
#    print(item)

# 12-2.3 bingo
#for item in letter_set(anagrams):
#    if letter_set(anagrams)[item] > 7:
#        print(item, letter_set(anagrams)[item])
