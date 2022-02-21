""" Reads text of a book from a file, skipping over the header and trailing information at the beginning and end,
    storing words in a dictionary. Counts and prints the total words and their frequencies. Creates a reference list
    by reading from a file. Processes Author objects with data members as location of the book, vocabulary,
    total different words, their frequency, 20 most-used, and vocabulary words not in a reference list. """

import string


mtrx = {"whit": {"leav":  ("/Users/hejtor/OneDrive/CS/ThinkPython stuff/whitman_leaves.txt",
                           "*** START OF THE PROJECT GUTENBERG EBOOK LEAVES OF GRASS ***",
                           "*** END OF THE PROJECT GUTENBERG EBOOK LEAVES OF GRASS ***")},
        "gibr": {"proph": ("/Users/hejtor/OneDrive/CS/ThinkPython stuff/gibran_prophet.txt",
                           "*** START OF THE PROJECT GUTENBERG EBOOK THE PROPHET ***",
                           "*** END OF THE PROJECT GUTENBERG EBOOK THE PROPHET ***")},
        "shak": {"sonn":  ("/Users/hejtor/OneDrive/CS/ThinkPython stuff/shakesp_sonnets.txt",
                           "*** START OF THE PROJECT GUTENBERG EBOOK THE SONNETS ***",
                           "*** END OF THE PROJECT GUTENBERG EBOOK THE SONNETS ***")},
        "tria": {"bitch": ("/Users/hejtor/OneDrive/CS/ThinkPython stuff/test_paragraph.txt",
                           "*** START OF THE PROJECT GUTENBERG EBOOK THE BITCH ***",
                           "*** END OF THE PROJECT GUTENBERG EBOOK THE BITCH ***")}
        }


def clean_n_store(dirty_word, temp_vocab):
    """ Removes punctuation and whitespace from a given string and stores it in a given dictionary. """

    pre_word = dirty_word.replace('“', '').replace('”', '').strip(string.punctuation).lower()
    if pre_word != "":
        if "--" not in pre_word:
            temp_vocab[pre_word] = temp_vocab.get(pre_word, 0) + 1
        else:
            clean_n_store(pre_word[:pre_word.index("--")], temp_vocab)
            clean_n_store(pre_word[pre_word.index("--") + 2:], temp_vocab)


def read_n_strip(file, beg, end, vocab):
    """ Reads lines from a file within a range of given beginning and ending lines.
        Calls clean_n_store to clean and store the words-to-be from those lines. """

    read = False
    fin = open(file)
    for line in fin:
        if line.strip() == end:
            return
        if line.strip() == beg:
            read = True
            continue
        if read:
            for word_to_be in line.split():
                clean_n_store(word_to_be, vocab)


def take_sec(tupel):
    """ Provides key to sorted function. """

    return tupel[1]     # sort by second item


def word_list():
    """ Reads a word list from a file.
        Output: set of strings """

    temp_list = set()
    fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
    for word in fin:                                # since there's only a word per line
        temp_list.add(word.strip())
    return temp_list


class Author:
    """ Creates an Author object with data members last_name, file_path, beg_line, end_line, vocab, and freq_list. """

    def __init__(self, last_name, book_title, file_path, beg_line, end_line):
        self.last_name = last_name
        self.book_title = book_title
        self.file_path = file_path                  # physical location of the book
        self.beg_line = beg_line                    # line before actual book content begins
        self.end_line = end_line                    # line book content ends
        self.vocab = {}
        self.vocab_length = 0
        self.freq_list = []
        self.twenty_most = []
        self.not_in_list = set()

        read_n_strip(self.file_path, self.beg_line, self.end_line, self.vocab)
        self.vocab_length = len(self.vocab)
        self.freq_list = sorted(sorted([(word, self.vocab[word]) for word in self.vocab]), key=take_sec, reverse=True)
        self.twenty_most = [tupel[0] for tupel in self.freq_list[:20]]
        words_list = word_list()
        self.not_in_list = {key for key in self.vocab if key not in words_list}


# print(word_list())

# shak = Author("Shakespeare", "Sonnets", mtrx["shak"]["sonn"][0], mtrx["shak"]["sonn"][1], mtrx["shak"]["sonn"][2])
# whit = Author("Whitman", "Leaves", mtrx["whit"]["leav"][0], mtrx["whit"]["leav"][1], mtrx["whit"]["leav"][2])
gibr = Author("Gibran", "Prophet", mtrx["gibr"]["proph"][0], mtrx["gibr"]["proph"][1], mtrx["gibr"]["proph"][2])
# tria = Author("Justi", "Bitch", mtrx["tria"]["bitch"][0], mtrx["tria"]["bitch"][1], mtrx["tria"]["bitch"][2])

# print(shak.last_name, "used in", shak.book_title, shak.vocab_length, "total different words.")
# print(shak.freq_list)
# print(shak.twenty_most)

# print(whit.last_name, "used in", whit.book_title, whit.vocab_length, "total different words.")
# print(whit.freq_list)
# print(whit.twenty_most)

# print(gibr.last_name, "used in", gibr.book_title, gibr.vocab_length, "total different words.")
# print(gibr.freq_list)
# print(gibr.twenty_most)
# print(gibr.vocab)
print(gibr.not_in_list)

# print(tria.vocab)
# print(tria.not_in_list)
