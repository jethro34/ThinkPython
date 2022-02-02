import time


def append_list_builder():
    w_list = []
    time1 = time.time()
    for i in range(100):
        fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
        for line in fin:
            w_list.append(line.strip())
    print(time.time() - time1)


def idiom_list_builder():
    w_list = []
    time1 = time.time()
    for i in range(100):
        fin = open("/Users/hejtor/OneDrive/CS/ThinkPython stuff/words.txt")
        for line in fin:
            w_list += [line.strip()]
    print(time.time() - time1)


append_list_builder()
# idiom_list_builder()
