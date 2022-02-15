"""
Finds all metathetic pairs of words in a list.
Logical steps:
    1. Create a dictionary by (forming letters) and [words formed with those letters]
    2. Check for methatetic pairs in [words formed with those letters] and add pairs to a list.
"""


def forming_letters(wort):
    """ Takes in a word and returns its letters sorted.
        Output: tuple """

    return tuple(sorted(wort))


def create_dict_from_file(file):
    """ Reads words from a file and creates a dictionary whose keys are forming letters and values words.
        Output: dictionary of the type (tuple): [list] """

    fin = open(file)
    for line in fin:
        w1 = line.strip()
        w2 = forming_letters(w1)
        forming_letters_dict.setdefault(w2, []).append(w1)


def are_metathetic(st1, st2):
    """ Checks whether two words are metathetic and adds them to a list if they are. """

    counter = 0

    for ch1, ch2 in zip(st1, st2):
        if ch1 != ch2:
            counter += 1

    if counter == 2:                            # two words are metathetic if they have only 2 characters swapped
        metathetic_pairs.append((st1, st2))


def combine_pairs(l1):
    """ Finds every pair in a list of elements. """

    lange = len(l1)

    for i in range(lange):
        for j in range(1, lange):
            if i < j:
                are_metathetic(l1[i], l1[j])


forming_letters_dict = {}
metathetic_pairs = []

create_dict_from_file("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

for item in forming_letters_dict:                       # combing dictionary of forming letters
    if len(forming_letters_dict[item]) > 1:             # filtering out [lists of words formed] of one item
        combine_pairs(forming_letters_dict[item])       # producing pairs of words to check for metathesis

print('there are', len(metathetic_pairs), 'metathetic pairs:')

metathetic_pairs.sort()

for item in metathetic_pairs:
    print(item)
