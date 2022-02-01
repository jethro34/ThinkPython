def is_palindrome(zahl, index1, index2):
    """Checks for palindromy in a given number after adding left zeros up to 6 digits within a given range."""
    s = str(zahl).zfill(6)[index1:index2]
    return s == s[::-1]


counter = 0

for n in range(999997):
    if is_palindrome(n, 2, 6):
        if is_palindrome(n + 1, 1, 6):
            if is_palindrome(n + 2, 1, 5):
                if is_palindrome(n + 3, 0, 6):
                    counter += 1
                    print("found: ", str(n).zfill(6), str(n + 1).zfill(6), str(n + 2).zfill(6), str(n + 3).zfill(6))

if counter == 0:
    print("no numbers found.")
