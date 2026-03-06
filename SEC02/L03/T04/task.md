# List Methods

## What You'll Learn

How to use built-in list methods to add, remove, count, and clear elements from a list.

## Concept Overview

Python lists come with powerful built-in methods that allow you to manipulate list contents without writing complex logic. These methods provide a clean, readable way to perform common operations like adding items at specific positions, removing items by value, counting occurrences, and emptying lists entirely.

Understanding these methods is essential for efficient list manipulation in Python. They handle the underlying complexity of list operations, making your code more maintainable and less error-prone.

## Key Concepts

### Adding Elements

Lists provide multiple methods for adding elements. The `append()` method adds an item to the end, while `insert()` allows you to place an item at a specific position by providing an index. These methods modify the list in place rather than creating a new list.

### Removing Elements

You can remove elements from a list in several ways. The `remove()` method searches for the first occurrence of a value and removes it. The `clear()` method removes all elements, leaving an empty list. Unlike del or pop, remove() works with values rather than indices.

### Querying Lists

The `count()` method tells you how many times a specific value appears in a list. This is useful for analyzing list contents without manually iterating through elements.

## Example

```python
inventory = ["hammer", "nails", "screwdriver"]

# Add item at the end
inventory.append("wrench")
print(inventory)  # ['hammer', 'nails', 'screwdriver', 'wrench']

# Add item at specific position
inventory.insert(1, "drill")
print(inventory)  # ['hammer', 'drill', 'nails', 'screwdriver', 'wrench']

# Remove specific item by value
inventory.remove("nails")
print(inventory)  # ['hammer', 'drill', 'screwdriver', 'wrench']

# Count occurrences
inventory.append("hammer")
count = inventory.count("hammer")
print(count)  # 2

# Clear all items
inventory.clear()
print(inventory)  # []
```

## Your Task

You'll practice using various list methods to manipulate a list. This involves adding items at different positions, removing specific items, counting occurrences, and clearing the list completely.
