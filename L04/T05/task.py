# Square Task
my_list = [5, 4, 3]

# Use map and lambda to create a list of squared numbers
answer_1 = list(map(lambda item: item * item, my_list))


# List Sorting Task
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

# Sort the list by the second element of each tuple
a.sort(key=lambda x: x[1])

