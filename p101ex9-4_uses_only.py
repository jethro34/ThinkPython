def uses_only(wort, req_letts):
    """Returns True if word contains only the letters in the list."""
    for c in wort:
        if c not in req_letts:
            return False
    return True


fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

req_letters = input("enter only possible letters in the words: ")

counter = 0
req_counter = 0

for line in fin:
    counter += 1
    word = line.strip()
    if uses_only(word, req_letters):
        req_counter += 1
        print(word)

print(req_counter, "words contain only the letters ", req_letters)
