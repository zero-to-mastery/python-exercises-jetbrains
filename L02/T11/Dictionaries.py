# Dictionaries Exercise

# Create a user profile for your new game.
# Store it in a dictionary:
user_profile = {
    'age': 0,
    'username': '',
    'weapons': None,
    'is_active': False,
    'clan': None
}

# Get all the keys from user_profile and convert them to a list
answer_1 = list(user_profile.keys())

# Set the value under key 'weapons' to 'Katana'
user_profile['weapons'] = 'Katana'
answer_2 = user_profile['weapons']

# Add a new key 'is_banned' and set it to False
user_profile.update({'is_banned': False})
answer_3 = user_profile['is_banned']

# Change the value under key 'is_banned' to True
user_profile['is_banned'] = True
answer_4 = user_profile['is_banned']

# Copy user_profile into user2 (create a new dictionary)
user2 = user_profile.copy()

# Change age to 50 and username to 'User2' only in user2
user2.update({'age': 50, 'username': 'User2'})
answer_5 = user2