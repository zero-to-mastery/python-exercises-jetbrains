# For Loops and Iteration

## What You'll Learn

How to use for loops to iterate over sequences like strings, lists, sets, and tuples, and how to create nested loops.

## Concept Overview

For loops allow you to iterate over any iterable object in Python, executing a block of code for each element. This is fundamental for processing collections of data, whether you're working with strings, lists, sets, tuples, or other iterable types.

Python's for loops are designed to work with any object that supports iteration, making them more flexible than traditional counter-based loops in other languages. You can iterate directly over values without managing indices.

## Key Concepts

### Iterating Over Different Types

A for loop can iterate over various iterable types. Iterating over a string processes each character, iterating over a list processes each element, and iterating over a set or tuple works similarly. The loop variable takes on each value in sequence.

### Loop Variable Scope

The loop variable (often called the iterator) is assigned each value from the iterable in turn. This variable remains accessible after the loop completes, holding the last value from the iteration.

### Nested Loops

You can place one loop inside another to create nested iterations. The inner loop completes all its iterations for each single iteration of the outer loop. This is useful for working with multi-dimensional data or creating combinations of elements from different collections.

## Example

```python
# Iterating over a string
word = "Python"
for letter in word:
    print(letter)  # P, y, t, h, o, n

# Iterating over a list
colors = ['red', 'green', 'blue']
for color in colors:
    print(color)

# Iterating over a set
numbers = {10, 20, 30}
for num in numbers:
    print(num)  # Order not guaranteed

# Nested loops
sizes = ['small', 'medium', 'large']
colors = ['red', 'blue']

for size in sizes:
    for color in colors:
        print(f"{size} {color}")
# Output: small red, small blue, medium red, medium blue, large red, large blue
```

## Your Task

You'll practice writing for loops that iterate over different types of collections and create nested loops to work with multiple iterables.
