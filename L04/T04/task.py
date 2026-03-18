from functools import reduce

# Functional Programming
# Complete the code below

my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

# Use map and list to capitalize all pet names
answer_1 = list(map(capitalize, my_pets))


my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

# Use zip, sorted, and list to combine my_strings with my_numbers from lowest to highest
answer_2 = list(zip(my_strings, sorted(my_numbers)))


scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

# Use filter and list to keep only the scores above 50
answer_3 = list(filter(is_smart_student, scores))


def accumulator(acc, item):
    return acc + item

# Use reduce to calculate the total of my_numbers and scores
answer_4 = reduce(accumulator, my_numbers + scores)