# List Comprehension and Sets
# Complete the code below

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Find all duplicated values in some_list.
# Use a list comprehension and set()
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))