# Dictionaries Exercise

dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

# Access the second number from the list under key 'a'
answer_1 = dictionary['a'][1]


# Dictionary methods
user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

# Get 'age' using get(), with default 55
answer_2 = user.get('age', 55)

# Create a dict with key 'name' and value 'JohnJohn'
user2 = dict(name='JohnJohn')

# Membership checks (keys)
answer_3 = 'basket' in user
answer_4 = 'size' in user

# Check keys/values/items
answer_5 = 'age' in user.keys()
answer_6 = 'Hello' in user.values()
answer_7 = dict(user).items()

# Copy the dictionary
answer_8 = user.copy()

# Make a separate copy for future changes
user_copy = user.copy()

# Clear the original dictionary
user.clear()
answer_9 = user

# Pop and update
answer_10 = user_copy.pop('age')
answer_11 = user_copy.popitem()

# Set the key 'age' to 55 in user_copy
user_copy.update({'age': 55})
answer_12 = user_copy