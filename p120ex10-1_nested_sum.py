def nested_sum(list_of_lists):
    accumulator = 0
    for listx in list_of_lists:
        accumulator += sum(listx)
    return accumulator


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
