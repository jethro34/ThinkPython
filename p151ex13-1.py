
words = []


def clean_word(w2):
    w3 = ''
    for ch in w2:
        if ch.isalpha() or (ch == '-' and w3[0].isalpha()):
            w3 += ch
    return w3.lower()


def words_from_line(l1):
    for w4 in l1:
        words.append(clean_word(w4))


def read_n_strip(file):
    fin = open(file)
    for line in fin:
        temp_words = line.strip().split()
        words_from_line(temp_words)


read_n_strip("/Users/hejtor/OneDrive/CS/ThinkPython stuff/test_paragraph.txt")

print(words)
