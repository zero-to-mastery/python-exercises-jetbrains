# Tuples Exercise

my_tuple = (1, 2, 3, 4, 5)

# Get the second element from the tuple
answer_1 = my_tuple[1]

# Check if 5 is inside the tuple (True/False)
answer_2 = 5 in my_tuple

# Unpack the tuple:
# x gets the first item, y gets the second, z gets the third,
# and 'other' gets a list of the remaining items
x, y, z, *other = my_tuple

answer_3 = x
answer_4 = z
answer_5 = other

# Count how many times 5 appears in my_tuple
answer_6 = my_tuple.count(5)

# Find the index of value 5 in my_tuple
answer_7 = my_tuple.index(5)