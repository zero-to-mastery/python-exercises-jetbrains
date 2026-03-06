# Finding Duplicates with Loops

## What You'll Learn

How to use nested loops or list methods to identify and collect duplicate values from a list.

## Concept Overview

Finding duplicates in a collection is a common data analysis task. It requires checking if elements appear more than once and collecting those duplicates without repeating them in your result. This can be accomplished through various approaches: using the count() method, nested loops for comparison, or set-based techniques.

This problem teaches important concepts like avoiding duplicate entries in your results, efficiently checking for repeated values, and understanding different algorithmic approaches to the same problem with varying performance characteristics.

## Key Concepts

### Using count() Method

The list count() method returns how many times a value appears in the list. By checking if count is greater than 1, you can identify duplicates. However, you must also ensure you don't add the same duplicate value to your results multiple times.

### Tracking Already Found Duplicates

When iterating through a list to find duplicates, you need a way to track which duplicate values you've already identified. This prevents adding the same duplicate to your results list multiple times. You can check if a value is already in your duplicates list before adding it.

### Alternative Approaches

Nested loops compare each element with all subsequent elements to find matches. Set-based approaches can leverage the uniqueness property of sets. Different algorithms have different time complexity trade-offs, with some being more efficient for large datasets.

## Example

```python
# Using count() with tracking
items = ['x', 'y', 'z', 'y', 'w', 'x', 'y']
duplicates = []

for item in items:
    if items.count(item) > 1:  # Appears more than once
        if item not in duplicates:  # Not already in results
            duplicates.append(item)

print(duplicates)  # ['x', 'y']

# Using nested loops
data = [5, 10, 15, 10, 20, 5]
dupes = []

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] == data[j] and data[i] not in dupes:
            dupes.append(data[i])

print(dupes)  # [5, 10]

# Using sets (most efficient)
numbers = [1, 2, 3, 2, 4, 1, 5]
seen = set()
duplicate_set = set()

for num in numbers:
    if num in seen:
        duplicate_set.add(num)
    else:
        seen.add(num)

print(list(duplicate_set))  # [1, 2]
```

## Your Task

You'll practice implementing duplicate detection by iterating through a list, using count() to identify values that appear more than once, and maintaining a results list that doesn't contain duplicate entries of the duplicates themselves.
