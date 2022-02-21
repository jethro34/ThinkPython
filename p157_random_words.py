
import random
from fractions import Fraction


def choose_from_hist(tupel):
    """ Takes a tuple of a histogram dictionary and a total of its values and returns a random key and its probability.
        Output: a tuple (string, string) """

    hist = sorted(tupel[0])
    zeichen = random.choice(hist)

    return zeichen, str(Fraction(tupel[0][zeichen], tupel[1]).limit_denominator())


def zeichen_im_wort(string):
    """ Takes a string and returns a histogram dictionary and a total of its values.
        Output: tuple of a dictionary and an integer """

    dikt = {}
    for zeichen in string:
        dikt[zeichen] = dikt.get(zeichen, 0) + 1

    return dikt, sum(dikt.values())


def random_word(dikt_hist):
    """ Randomly chooses a word from a given histogram dictionary by creating a list with each element timed
        by its number of instances.
        Output: a string """

    l2 = []
    for item in dikt_hist:
        l2.extend([item] * dikt_hist[item])

    return random.choice(l2)


def random_word2(s1):
    """ Randomly chooses a character from a given string.
        Output: a string """

    return s1[random.randint(0, len(s1) - 1)]


d = zeichen_im_wort('eresputamuyputaputissima')
# print(d)

# print(choose_from_hist(d))
# print(random_word(d[0]))
print(random_word2('eresputamuyputaputissima'))
