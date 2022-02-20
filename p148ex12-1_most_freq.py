def take_second(t):
    """ Sets sorted's key to the second item of the tuple."""

    return t[1]


def most_freq(stx):
    """ Takes a string and prints the letters in decreasing order of frequency."""

    dikt = {}

    for char in stx:
        if not char.isalpha():
            continue
        dikt[char] = dikt.get(char, 0) + 1                           # creating dict entry by letter

    tup_list = list(dikt.items())                                           # creating a list of tuples from dict
    tup_list_alpha = sorted(tup_list)                                       # sorting in alphabetical order
    tup_list_freq = sorted(tup_list_alpha, key=take_second, reverse=True)   # sorting by frequency
    print(tup_list_freq)


most_freq("you're a very disrespectful bitch!")
most_freq("eres una peleona falta de respeto!")
