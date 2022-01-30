def is_anagram(str1, str2):
    """Checks for anagramy between two given strings."""
    return len(str1) == len(str2) and sorted(str1) == sorted(str2)


print(is_anagram("mamma", "ammam"))
