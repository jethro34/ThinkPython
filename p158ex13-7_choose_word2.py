
import string
import random


def read_n_strip(file):
    fin = open(file)
    for line in fin:
        for pre_word in line.replace("--", " ").split():
            word = pre_word.strip(string.punctuation + string.whitespace).lower()
            if word != '':
                hist_dikt[word] = hist_dikt.get(word, 0) + 1


def create_lists(dikt):
    total_freq = 0
    for word, hits in dikt.items():
        total_freq += hits
        words_list.append(word)
        freq_sum.append(total_freq)


def find_index(zahl, liste):
    """ Finds the number immediately bigger/equal to the given target in a given list of numbers and returns its index,
        using bisection.
        Output: integer """

    bisect = len(liste) // 2
    if zahl <= liste[0]:
        return 0
    if zahl == liste[bisect]:
        return bisect
    if zahl > liste[bisect]:
        return find_index(zahl, liste[bisect + 1:]) + bisect + 1
    else:
        return find_index(zahl, liste[1: bisect + 1]) + 1


hist_dikt = {}
words_list = []
freq_sum = []

read_n_strip("/Users/hejtor/OneDrive/CS/ThinkPython stuff/test_paragraph.txt")

create_lists(hist_dikt)

x = random.randint(1, freq_sum[-1])                             # generating the random number
print("the random freq is:", x)
print("the index of", x, "is", find_index(x, freq_sum))
print("and the word is:", words_list[find_index(x, freq_sum)])
