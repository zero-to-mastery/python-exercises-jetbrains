# Sorting Lists and Method Return Values

## What You'll Learn

How to combine list methods and understand the difference between methods that modify lists in-place versus those that return new values.

## Concept Overview

In Python, some list methods modify the list directly and return None, while others return a new value without changing the original list. Understanding this distinction is crucial for writing correct code, especially when chaining operations or combining lists.

The `sort()` method sorts a list in-place and returns None, while the `sorted()` function returns a new sorted list without modifying the original. Similarly, methods like `extend()` combine lists in-place, allowing you to chain operations correctly.

## Key Concepts

### In-Place vs Returning Methods

Methods like `sort()` modify the list directly and return None. This means you cannot use their return value in expressions. In contrast, functions like `sorted()` return a new sorted list, leaving the original unchanged. Choosing the right approach depends on whether you need to preserve the original list.

### Extending Lists

The `extend()` method adds all elements from one list to another list in-place. Unlike concatenation with the + operator, extend modifies the existing list rather than creating a new one. This is more memory efficient when you want to merge lists permanently.

### Method Chaining Pitfalls

Because many list methods return None, trying to chain them or use their return values in expressions will cause errors. You must separate the modification step from any operations that need the modified value.

## Example

```python
numbers = [5, 2, 8, 1, 9]
more_numbers = [3, 7]

# Wrong: sort() returns None, can't concatenate
# result = numbers.sort() + more_numbers  # Error!

# Correct: sort first, then concatenate
numbers.sort()
result = numbers + more_numbers
print(result)  # [1, 2, 5, 8, 9, 3, 7]

# Alternative: use sorted() which returns a new list
numbers = [5, 2, 8, 1, 9]
result = sorted(numbers) + more_numbers
print(result)  # [1, 2, 5, 8, 9, 3, 7]

# Using extend to merge lists
numbers = [5, 2, 8, 1, 9]
numbers.extend(more_numbers)
numbers.sort()
print(numbers)  # [1, 2, 3, 5, 7, 8, 9]
```

## Your Task

You'll practice fixing code that incorrectly uses list methods, understanding when methods return None versus new values, and how to properly combine and sort lists.
