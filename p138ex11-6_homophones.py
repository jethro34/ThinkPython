def read_dictionary():
    """Reads from a file and builds a dictionary that maps from
    each 4 & 5-letter word to a string that describes its primary pronunciation."""
    d = dict()
    fin = open('/Users/hejtor/OneDrive/CS/ThinkPython stuff/c06d.txt')
    for line in fin:
        if not line[0].isalpha():
            continue
        t = line.split()
        word = t[0].lower()
        if 4 <= len(word) <= 5:
            pron = ' '.join(t[1:])
            d[word] = pron
    return d


d = read_dictionary()

for w1 in d:
    if len(w1) == 5:
        w2, w3 = w1[1:], w1[0] + w1[2:]
        if w2 in d and w3 in d and d[w1] == d[w2] and d[w1] == d[w3]:
            print(w1, w2, w3)
