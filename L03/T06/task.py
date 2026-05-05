# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)
