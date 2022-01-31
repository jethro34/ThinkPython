fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")

for line in fin:
    if len(line.strip()) > 20:
        print(line.strip())
