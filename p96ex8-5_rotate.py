
def rotate_character(character, integer):
    if character.islower():
        return chr((ord(character) - 97 + integer) % 26 + 97)
    if character.isupper():
        return chr((ord(character) - 65 + integer) % 26 + 65)
    else:
        return character


def rotate_word(string, integer):
    temp = ""
    for character in string:
        temp += rotate_character(character, integer)
    return temp


print(rotate_word('Donna is a bitch', -27))
