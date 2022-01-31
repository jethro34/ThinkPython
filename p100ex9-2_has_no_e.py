def has_no_e(string):
    return 'e' not in string


fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

counter = 0
e_less = 0

for line in fin:
    counter += 1
    word = line.strip()
    if has_no_e(word):
        e_less += 1
        print(word)

print(e_less / counter * 100, "of the words have no 'e'.")
