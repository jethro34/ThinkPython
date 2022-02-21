
import random
from fractions import Fraction


def choose_from_hist(tupel):
    """ Takes a tuple of a histogram dictionary and a total of its values and returns a random key and its probability.
        Output: tuple of two strings """

    hist = sorted(tupel[0])
    zeichen = random.choice(hist)

    return zeichen, str(Fraction(tupel[0][zeichen], tupel[1]).limit_denominator())


def zeichen_im_wort(string):
    """ Takes a string and returns a histogram dictionary and a total of its values.
        Output: tuple of a dictionary and an integer """

    zahler = 0
    dikt = {}
    for zeichen in string:
        dikt[zeichen] = dikt.get(zeichen, 0) + 1
        zahler += 1

    return dikt, zahler


d = zeichen_im_wort('eresputamuyputaputissima')
print(d)

print(choose_from_hist(d))
