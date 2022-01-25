def first(string):
    return string[0]


def last(string):
    return string[-1]


def middle(string):
    return string[1: -1]


def is_palindrome(string):
    """Checks for palindromy."""
    if first(string) == last(string):
        if middle(string) == "":
            return True
        return is_palindrome(middle(string))
    return False


print(is_palindrome("anna"))
