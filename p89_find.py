def find(word, letter, index=1):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


print(find('bitch', 'z'))