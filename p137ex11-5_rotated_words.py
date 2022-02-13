""" Creates a word list and checks for rotated words."""


known_seq = {}


def create_list():
    """ Creates a list by reading from a file.
        Output: list."""
    w_list = []
    fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
    for line in fin:
        w_list.append(line.strip())
    return w_list


def seq(wort):
    """ Finds the numeric sequence of the characters in a word.
        Output value: tuple."""
    liste = []
    for i in range(len(wort) - 1):
        liste.append(ord(wort[i + 1]) - ord(wort[i]))
    return tuple(liste)


def check_word(wort):
    """ Checks/stores a word's sequence in a dictionary."""
    known_seq.setdefault(seq(wort), []).append(wort)


def find_rotated_words(liste):
    """ Finds rotated words in a list."""
    for i in range(len(liste)):
        check_word(liste[i])


liste = create_list()
find_rotated_words(liste)

for item in known_seq:
    if len(known_seq[item]) > 1:
        print(known_seq[item])
