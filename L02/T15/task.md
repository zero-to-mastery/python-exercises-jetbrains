# Dictionary Methods

## Theory

When you read data from a dictionary, there are a few tools that help you do it safely and conveniently.

### Safe access

`dict.get(key, default)` returns the value for `key`. If the key is missing, it returns the `default` value instead of raising an error. If you don’t pass a default, missing keys return `None`.

### Key existence

The `in` operator checks for keys by default. For example, `'basket' in user` is `True` if `'basket'` is a key in the dictionary, and `False` otherwise. This is a quick way to test whether a key exists before you try to access it.

### Views and order

`dict.values()` returns a view of all values stored in the dictionary. You can use `in` with it to check whether a specific value exists, for example `'Hello' in user.values()`.

`dict.items()` returns a view of all key–value pairs as `(key, value)` tuples. Converting it to a list with `list(user.items())` gives you a regular list of tuples, which is often easier to inspect, compare in tests, or loop over. In modern Python, keys/values/items keep the insertion order of the dictionary.
