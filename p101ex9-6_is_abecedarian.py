def is_abecedarian(wort):
    """Returns True if the letters in a given word appear in alphabetical order."""
    for i in range(len(wort) - 1):
        if wort[i] > wort[i + 1]:
            return False
    return True


fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

counter = 0
abc_counter = 0

for line in fin:
    counter += 1
    word = line.strip()
    if is_abecedarian(word):
        abc_counter += 1
        print(word)

print(abc_counter, "words have their letters in alphabetical order.")
