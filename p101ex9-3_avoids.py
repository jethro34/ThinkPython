def avoids(string, forbidden):
    for c in forbidden:
        if c in string:
            return False
    return True


fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

forbidden_in = input("enter letters you want to forbid: ")

counter = 0
forb_counter = 0

for line in fin:
    counter += 1
    word = line.strip()
    if avoids(word, forbidden_in):
        forb_counter += 1
        print(word)

print(forb_counter, "words don't have any of the letters in", forbidden_in)
