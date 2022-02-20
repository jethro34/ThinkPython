""" Reads text of a book from a file, skipping over the header and trailing information at the beginning and end,
    storing words in a dictionary. Counts and prints the total words and their frequencies.
    Compares different books by different authors, written in different eras.
    Which author uses the most extensive vocabulary? """

import string

words = {}


def clean_n_store(word):
    pre_word = word.strip(string.punctuation).lower()
    if pre_word != "":
        if "--" not in pre_word:
            words[pre_word] = words.get(pre_word, 0) + 1
        else:
            clean_n_store(pre_word[:pre_word.index("--")])
            clean_n_store(pre_word[pre_word.index("--") + 2:])


def read_n_strip(file):
    read = False
    fin = open(file)
    for line in fin:
        if line.strip() == '*** END OF THE PROJECT GUTENBERG EBOOK LEAVES OF GRASS ***':
            return
        if line.strip() == '*** START OF THE PROJECT GUTENBERG EBOOK LEAVES OF GRASS ***':
            read = True
            continue
        if read:
            for word in line.split():
                clean_n_store(word)


def take_second(tupel):
    """ Provides key to sorted function. """
    return tupel[1]     # sort by second item


read_n_strip("/Users/hejtor/OneDrive/CS/ThinkPython stuff/whitman_leaves.txt")

print(len(words), "total words:")

test = sorted(sorted([(word, words[word]) for word in words]), key=take_second, reverse=True)
print(test)
