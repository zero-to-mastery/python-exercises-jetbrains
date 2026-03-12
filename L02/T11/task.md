# Working With Dictionaries

## Theory

A dictionary (`dict`) is a data structure for storing data as **key -> value** pairs. It is useful when you want to access information by a meaningful name (the key), not by position like in a list. A common example is storing information about a book, a product, or a student: keys like "title", "price", "grade" point to their values.

### Creating and accessing

You can create a dictionary with curly braces `{}` using `key: value` pairs. Keys are often strings, and values can be different types: numbers, strings, booleans, `None`, lists, or even other dictionaries.

To **read** a value, use square brackets with the key: `item['price']`. To **change** a value, assign to that key: `item['price'] = 10`. If the key does not exist yet, this assignment creates a new key in the dictionary.

### Inspecting keys

`dict.keys()` returns a view of all keys stored in the dictionary. If you need a regular list (for example, for tests or for printing), convert it with `list(item.keys())`.

### Updating

`dict.update(...)` updates the dictionary using another dictionary. It adds new keys and overwrites existing keys with new values. For example, `item.update({'in_stock': True, 'price': 12})` can add "in_stock" and also replace the current "price".

### Copying

`dict.copy()` creates a new dictionary with the same key-value pairs. This is useful when you want to make changes to a copy without modifying the original dictionary. (It is a shallow copy: nested mutable values like lists are still shared, but simple values like numbers and strings are copied safely.)
