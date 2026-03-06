# Dictionary Manipulation Exercise

## What You'll Learn

How to build and modify complex dictionary structures by combining multiple dictionary operations.

## Concept Overview

Real-world applications often require creating dictionaries with specific structures and then modifying them through a series of operations. This involves creating keys with various value types, iterating through dictionary elements, adding new key-value pairs, updating existing values, and creating modified copies.

Mastering dictionary manipulation is essential for working with structured data like user profiles, configuration objects, API responses, or any scenario where you need to organize and update related information.

## Key Concepts

### Building Dictionary Structures

Creating a dictionary with a specific structure requires understanding what types of values each key should hold. Values can be simple types (numbers, strings, booleans) or complex types (lists, other dictionaries). Choosing the right structure depends on the data you need to represent.

### Iterating Dictionary Keys

The `keys()` method returns a view of all dictionary keys, which you can iterate through or convert to a list. This is useful for inspecting the structure of a dictionary or performing operations on all keys.

### Modifying and Updating

You can add new keys using bracket notation or the `update()` method. Bracket notation works for single key-value pairs, while `update()` can add multiple pairs at once. Both approaches will overwrite existing keys with the same name.

### Copying and Modifying

The `copy()` method creates a shallow copy of a dictionary. This allows you to create a modified version without affecting the original. After copying, you can use `update()` to change multiple values efficiently.

## Example

```python
# Creating a structured dictionary
employee = {
    'id': 0,
    'name': '',
    'department': None,
    'is_manager': False,
    'projects': None
}

# Iterating through keys
for key in employee.keys():
    print(key)

# Adding new data
employee['department'] = 'Engineering'
employee['projects'] = ['Project A']

# Adding a new key
employee.update({'hire_date': '2024-01-15'})

# Modifying existing value
employee['is_manager'] = True

# Creating a modified copy
manager = employee.copy()
manager.update({'id': 100, 'name': 'Sarah'})

print(employee)
print(manager)
```

## Your Task

You'll practice creating a dictionary with a specific structure, iterating through its keys, adding new values to existing keys, adding entirely new keys, modifying existing values, and creating modified copies of dictionaries.
