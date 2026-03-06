# Tuples

## What You'll Learn

How to use tuples, an immutable sequence type in Python, and understand their properties and methods.

## Concept Overview

Tuples are ordered, immutable sequences similar to lists but with a key difference: once created, their contents cannot be changed. This immutability makes tuples useful for data that shouldn't be modified, such as coordinates, configuration values, or function return values with multiple items.

Tuples use parentheses instead of square brackets and support many of the same operations as lists, including indexing, slicing, and membership testing. However, they have fewer methods because they cannot be modified after creation.

## Key Concepts

### Immutability

Unlike lists, tuples cannot be modified after creation. You cannot add, remove, or change elements. This property makes tuples safer for data that should remain constant and slightly more memory-efficient than lists. When you need unchangeable data, tuples are the appropriate choice.

### Tuple Unpacking

Tuples support unpacking, allowing you to assign multiple variables at once from a tuple's elements. You can use the * operator to collect remaining elements into a list. This pattern is commonly used for function returns and multiple assignments.

### Limited Methods

Because tuples are immutable, they have only two methods: `count()` to count occurrences of a value, and `index()` to find the position of a value. This limited interface reflects their purpose as fixed collections.

## Example

```python
# Creating a tuple with coordinates
location = (40.7128, -74.0060, "New York")

# Accessing elements by index
latitude = location[0]
print(latitude)  # 40.7128

# Unpacking
lat, lon, city = location
print(city)  # New York

# Using * to collect remaining values
x, y, *rest = (1, 2, 3, 4, 5)
print(rest)  # [3, 4, 5]

# Tuple methods
coordinates = (10, 20, 10, 30)
print(coordinates.count(10))  # 2
print(coordinates.index(20))  # 1

# Membership testing
print(30 in coordinates)  # True
```

## Your Task

You'll practice working with tuples by accessing elements, using tuple unpacking, and exploring the available tuple methods like count() and index().
