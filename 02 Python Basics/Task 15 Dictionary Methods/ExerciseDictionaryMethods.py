# Getting data from a dictionary Exercise

user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

# Get the value under key 'age' using .get(). If there is no 'age', use 55.
answer_1 = user.get('age', 55)

# Check if there is a key 'basket' in user (True/False).
answer_2 = 'basket' in user

# Check if there is a key 'size' in user (True/False).
answer_3 = 'size' in user

# Check if there is a value 'Hello' in user (True/False).
answer_4 = 'Hello' in user.values()

# Get all key-value pairs from user using .items() and convert them to a list.
answer_5 = list(user.items())