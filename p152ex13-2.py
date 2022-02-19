""" Reads text from a file, skipping over the header and trailing information at the beginning and end of the file,
    storing words in a list. """
# Next: count the total number of words in the book, and the number of times each word is used.
# Print the number of different words used in the book. Compare different books by different authors,
# written in different eras. Which author uses the most extensive vocabulary?

import string

words = []


def clean_word(word):
    pre_word = word.strip(string.punctuation)
    if pre_word != "":
        if "--" not in pre_word:
            words.append(pre_word.lower())
        else:
            words.append(pre_word[:pre_word.index("--")].strip(string.punctuation).lower())
            clean_word(pre_word[pre_word.index("--") + 2:])


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
                clean_word(word)


read_n_strip("/Users/hejtor/OneDrive/CS/ThinkPython stuff/whitman_leaves.txt")

print(words)
