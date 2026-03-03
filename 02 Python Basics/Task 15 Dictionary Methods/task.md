# Dictionary Methods

## Working with Dictionary Methods

Dictionaries come with powerful methods for adding, accessing, modifying, and copying data. Understanding these methods is essential for effective Python programming.

## Essential Dictionary Methods

### keys()
Returns all dictionary keys as a view object (convertible to a list):
```python
user.keys()  # dict_keys(['age', 'username'])
```

### copy()
Creates a shallow copy of the dictionary. Changes to the copy don't affect the original:
```python
user2 = user.copy()
```

### Accessing Nested Values
When dictionary values are lists or other data structures, you can access and modify them using chaining:
```python
user['weapons'].append('sword')  # Adds to the list inside the dictionary
```

## Adding and Modifying Keys

Use bracket notation to add new keys or update existing ones:
```python
user['is_banned'] = False  # Adds new key
user['is_banned'] = True   # Updates existing key
```

## Practical Applications

Dictionaries are perfect for representing real-world entities like:
- User profiles with multiple attributes
- Game characters with stats and inventory
- Configuration settings
- API responses
