# Sets and Set Operations

## What You'll Learn

How to use sets to store unique values and perform mathematical set operations like unions, intersections, and differences.

## Concept Overview

Sets are unordered collections of unique elements. They automatically eliminate duplicates and provide efficient membership testing. Sets are particularly useful when you need to ensure uniqueness, remove duplicates from a list, or perform mathematical set operations like finding common elements between collections.

Python sets support operations like union (combining sets), intersection (finding common elements), difference (finding elements in one set but not another), and more. These operations make sets powerful tools for data analysis and comparison tasks.

## Key Concepts

### Uniqueness and Conversion

Sets automatically remove duplicate values. You can convert a list to a set to eliminate duplicates, then convert back to a list if needed. This is a common pattern for deduplication. Sets also provide `add()` to insert elements, which has no effect if the element already exists.

### Set Comparison Methods

Sets provide methods for comparing their contents: `difference()` returns elements in one set but not another, `intersection()` returns common elements, `union()` combines all unique elements from both sets, `issubset()` checks if all elements of one set exist in another, and `issuperset()` checks the opposite.

### Modifying Sets

Methods like `difference_update()` modify a set in place by removing elements that exist in another set. The `discard()` method removes an element if it exists without raising an error. The `clear()` method removes all elements, and `copy()` creates a shallow copy.

## Example

```python
# Creating sets and removing duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = set(numbers)
print(unique)  # {1, 2, 3, 4, 5}

# Adding elements
unique.add(6)
unique.add(3)  # No effect, already exists
print(unique)  # {1, 2, 3, 4, 5, 6}

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.difference(set_b))    # {1, 2}
print(set_a.intersection(set_b))  # {3, 4}
print(set_a.union(set_b))         # {1, 2, 3, 4, 5, 6}
print({1, 2}.issubset(set_a))     # True

# Modifying sets
set_a.discard(1)
print(set_a)  # {2, 3, 4}
```

## Your Task

You'll practice creating sets, using add() to insert elements, converting between sets and lists, creating copies, and applying set comparison methods like difference(), intersection(), union(), and various checking methods.
