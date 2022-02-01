def uses_all(wort, req_buchstaben):
    """Returns True if word contains all the letters in the list."""
    for c in req_buchstaben:
        if c not in wort:
            return False
    return True


fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

req_characters = input("enter only possible letters in the words: ")

counter = 0
req_counter = 0

for line in fin:
    counter += 1
    word = line.strip()
    if uses_all(word, req_characters):
        req_counter += 1
        print(word)

print(req_counter, "words contain all the letters in", req_characters)
