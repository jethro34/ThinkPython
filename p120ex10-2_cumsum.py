def cumsum(list1):
    accum = [list1[0]]
    for index in range(2, len(list1) + 1):
        accum.append(sum(list1[0:index]))
    return accum


t = [1, 4, 9]
print(cumsum(t))
