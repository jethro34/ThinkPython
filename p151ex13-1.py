# Reads a file, breaks each line into words, strips whitespace and punctuation from the words,
# and converts them to lowercase.

import string

words = []


def read_n_strip(file):
    fin = open(file)
    for line in fin:
        for word in line.split():
            if word.strip(string.punctuation) != '':
                words.append(word.strip(string.punctuation).lower())


read_n_strip("/Users/hejtor/OneDrive/CS/ThinkPython stuff/test_paragraph.txt")

print(words)

