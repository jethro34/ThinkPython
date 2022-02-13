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
    """ Takes in a forming-letter-to-word dictionary and turns out a frequency-organized list.
    Output: list of tuples """

    l1 = []
    for item in dikt:
        l1.append(tuple(dikt[item]))
    return sorted(l1, key=len, reverse=True)


# for item in anagram_dict(dict_from_file()):
#     print(anagram_dict(dict_from_file())[item])

for item in sort_freq(anagram_dict(dict_from_file())):
    print(item)
