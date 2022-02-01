def is_palindrome(zahl, index1, index2):
    print(str(zahl).zfill(6))
    print(str(zahl).zfill(6)[index1:index2], str(zahl).zfill(6)[index2:index1-1:-1])
    return str(zahl).zfill(6)[index1:index2] == str(zahl).zfill(6)[index2:index1-1:-1]


#n = 3
#print(str(n).zfill(6))

#print(is_palindrome(129923, 1, 5))

print('012345'[2:6], '012345'[5:1:-1])

print('012345'[1:6], '012345'[5:0:-1])

print('012345'[0:6], '012345'[::-1])


