# Sets Methods Exercise

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# Add 100 to my_set
my_set.add(100)
# Save a copy now, so answer_1 stays the same even if my_set changes later
answer_1 = my_set.copy()

# Check if {4, 5} is a subset of your_set (True/False)
answer_2 = {4, 5}.issubset(your_set)

# Check if your_set is a superset of {8, 9} (True/False)
answer_3 = your_set.issuperset({8, 9})

# Remove from my_set all elements that are also in your_set (change my_set in place)
my_set.difference_update(your_set)
answer_4 = my_set

# Remove 5 from my_set using discard()
my_set.discard(5)
answer_5 = my_set