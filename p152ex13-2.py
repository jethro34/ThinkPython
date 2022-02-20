""" Reads text of a book from a file, skipping over the header and trailing information at the beginning and end,
    storing words in a dictionary. Counts and prints the total words and their frequencies.
    Compares different books by different authors, written in different eras.
    Which author uses the most extensive vocabulary? """

import string


matrix = {'Whitman':  {"Leaves of Grass":  ("/Users/hejtor/OneDrive/CS/ThinkPython stuff/whitman_leaves.txt",
                                            "*** START OF THE PROJECT GUTENBERG EBOOK LEAVES OF GRASS ***",
                                            "*** END OF THE PROJECT GUTENBERG EBOOK LEAVES OF GRASS ***")}}


def clean_n_store(word):
    pre_word = word.strip(string.punctuation).lower()
    if pre_word != "":
        if "--" not in pre_word:
            vocabulary[pre_word] = vocabulary.get(pre_word, 0) + 1
        else:
            clean_n_store(pre_word[:pre_word.index("--")])
            clean_n_store(pre_word[pre_word.index("--") + 2:])


def read_n_strip(file, beg, end):
    read = False
    fin = open(file)
    for line in fin:
        if line.strip() == end:
            return
        if line.strip() == beg:
            read = True
            continue
        if read:
            for word in line.split():
                clean_n_store(word)


def take_second(tupel):
    """ Provides key to sorted function. """
    return tupel[1]     # sort by second item


class Author:
    """ Creates an Author object with data members last_name, file_path, beg_line, end_line, vocab, and freq_list. """

    def __init__(self, last_name, book_title, file_path, beg_line, end_line):
        self.last_name = last_name
        self.book_title = book_title
        self.file_path = file_path                  # physical location of the book
        self.beg_line = beg_line                    # line before actual book content begins
        self.end_line = end_line                    # line book content ends
        self.vocab = {}
        self.freq_list = []


vocabulary = {}

# read_n_strip("/Users/hejtor/OneDrive/CS/ThinkPython stuff/whitman_leaves.txt")

print(len(vocabulary), "total words:")

test = sorted(sorted([(word, vocabulary[word]) for word in vocabulary]), key=take_second, reverse=True)
print(test)
