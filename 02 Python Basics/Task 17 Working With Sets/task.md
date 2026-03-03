# Working With Sets

## What Are Sets?

Sets are **unordered collections of unique elements**. They automatically remove duplicates and are perfect for mathematical set operations like union, intersection, and difference.

```python
my_set = {1, 2, 3}
unique = {1, 2, 2, 3}  # Still becomes {1, 2, 3}
```

## Key Characteristics

### Uniqueness
Sets only store unique values - duplicates are automatically removed:
```python
numbers = {1, 2, 2, 3, 3, 3}  # Results in {1, 2, 3}
```

### Unordered
Unlike lists or tuples, sets have no defined order. Elements may appear in any sequence.

### Syntax
Use curly braces `{}` with comma-separated values. (Empty set requires `set()` - empty `{}` creates a dictionary!)

## Set Operations

### Union
Combines all elements from both sets (no duplicates):
```python
set1.union(set2)  # All unique elements from both sets
```

### Intersection
Returns only elements present in both sets:
```python
set1.intersection(set2)  # Common elements
```

### Difference
Returns elements in first set but not in second:
```python
set1.difference(set2)  # Elements unique to set1
```

## Set Methods

- **add()** - Adds a single element
- **in** - Checks if element exists (returns True/False)
- **remove()** / **discard()** - Removes elements

## Practical Use: Removing Duplicates

Convert a list to a set and back to remove duplicates:
```python
unique_items = list(set(items_with_duplicates))
```

## Your Task

Practice set operations:
1. Create sets with curly brace syntax
2. Use union, intersection, and difference operations
3. Add elements to sets
4. Check membership with `in`
5. Remove duplicates from a list using sets

**Challenge:** Why can't sets contain duplicate values?
