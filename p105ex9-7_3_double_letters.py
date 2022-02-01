def three_consec_pairs(wort):
    """Returns True if a given word has three consecutive double letters."""

    if len(wort) >= 6:
        for i in range(len(wort) - 5):
            if len(wort) - 1 >= 6:
                if (wort[i] == wort[i + 1]) and (wort[i + 2] == wort[i + 3]) and (wort[i + 4] == wort[i + 5]):
                    return True
    return False


fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

counter = 0
thcp_counter = 0

for line in fin:
    counter += 1
    word = line.strip()
    if three_consec_pairs(word):
        thcp_counter += 1
        print(word)

print(thcp_counter, "words have three consecutive double letters.")
