# Iterating Over Dictionaries

## What You'll Learn

How to iterate over dictionaries using various methods to access keys, values, or key-value pairs during iteration.

## Concept Overview

Dictionaries are iterable, but unlike lists, iterating over a dictionary directly yields only the keys. Python provides several methods to control what you iterate over: keys(), values(), or items() for key-value pairs. Understanding these options allows you to access dictionary data efficiently in loops.

The items() method is particularly powerful because it returns tuples of (key, value) pairs that you can unpack directly in your for loop, providing clean access to both pieces of information simultaneously.

## Key Concepts

### Default Dictionary Iteration

When you iterate over a dictionary directly without calling a method, Python iterates over the keys. This is equivalent to calling keys() explicitly. This behavior allows you to quickly access all keys for lookup or processing.

### Accessing Keys, Values, and Items

The keys() method returns a view of all keys, values() returns all values, and items() returns (key, value) tuples. These views are dynamic and reflect changes to the dictionary. Each method serves different iteration needs depending on what data you need to access.

### Tuple Unpacking with items()

When using items(), you can unpack the (key, value) tuple directly in the for statement: `for key, value in dict.items()`. This provides the most readable way to access both keys and values during iteration, avoiding the need for bracket notation lookups inside the loop.

## Example

```python
person = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 28,
    'city': 'Boston'
}

# Iterating over keys (default)
for key in person:
    print(key)  # first_name, last_name, age, city

# Explicit keys() - same as above
for key in person.keys():
    print(f"{key}: {person[key]}")

# Iterating over values only
for value in person.values():
    print(value)  # Jane, Doe, 28, Boston

# Iterating over key-value pairs
for key, value in person.items():
    print(f"{key} = {value}")
# Output: first_name = Jane, last_name = Doe, age = 28, city = Boston
```

## Your Task

You'll practice iterating over a dictionary using different methods: direct iteration over keys, using keys(), values(), items(), and unpacking key-value pairs in the loop.
