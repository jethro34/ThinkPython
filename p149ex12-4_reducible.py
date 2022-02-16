""" This program finds reducible words. """

words = {'': True, 'a': None, 'i': None}        # initializing the dictionary with the 'seeded' words
reducible_words = set()                         # initializing the set of reducible words


def add_words_to_dict_from(file):
    """ Reads (from a file) and adds words as keys to a dictionary with value 'None'. """

    fin = open(file)
    for line in fin:
        word = line.strip()
        words[word] = None


def is_reducible(parent):
    """ Checks if a word is reducible by recursively checking its children. """

    if type(words[parent]) == bool:             # checking whether parent word's reducibility is already known
        return words[parent]
    for i in range(len(parent)):                # creating children words if parent word's reducibility is unknown
        child = parent[:i] + parent[i + 1:]
        if child not in words:                  # filtering out children which aren't words
            continue
        if is_reducible(child):
            words[parent] = True                # setting parent word to True if a child is reducible
            return True
    words[parent] = False                       # setting parent word to False as non-reducible
    return False


add_words_to_dict_from("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

for w1 in words:
    is_reducible(w1)                            # testing every word for reducibility and updating status accordingly

for w2 in words:                                # adding reducible words from dictionary to a set
    if words[w2]:
        reducible_words.add(w2)

# print(reducible_words)

# print('the longest reducible word is:', max(reducible_words, key=len))

# print(sorted(reducible_words, key=len, reverse=True))
