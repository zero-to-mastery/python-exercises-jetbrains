# Logical Operators Exercise
# Complete the conditions using logical operators

is_magician = False
is_expert = True

# Use 'and' to check if someone is both a magician and an expert
answer_1 = is_magician and is_expert
if answer_1:
    # If answer_1 is True, this will print
    print("You are a master magician")

# Use 'and' with 'not' to check if someone is a magician but not an expert
answer_2 = is_magician and not is_expert
if answer_2:
    print("At least you\'re getting there.")

# Use 'not' to check if someone is not a magician
answer_3 = not is_magician
if answer_3:
    print("You need magic powers.")