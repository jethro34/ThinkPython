def count(string, letter, index=0):
    """Counts instances of letter in string."""

    counter = 0
    for char in string[index:]:
        if char == letter:
            counter += 1
    return counter


print(count("itchy bitchy bitch", "i", 0))
