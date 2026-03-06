# Changing a dictionary Exercise

user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

# Make a copy of user into user2
user2 = user.copy()
# Make a snapshot copy of user2 now, so answer_1 stays the same after user2 changes later
answer_1 = user2.copy()

# Remove key 'age' from user2 using pop(), and save the removed value in answer_2
answer_2 = user2.pop('age')

# Remove the last key-value pair from user2 using popitem(), and save that pair in answer_3
answer_3 = user2.popitem()

# Add/update key 'age' in user2 to be 55
user2.update({'age': 55})

# Clear user (make it empty)
user.clear()

answer_4 = user
answer_5 = user2