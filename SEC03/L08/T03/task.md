# The enumerate() Function

## What You'll Learn

How to use enumerate() to access both the index and value of items while iterating through a sequence.

## Concept Overview

The `enumerate()` function adds a counter to an iterable, allowing you to access both the position (index) and value of each element simultaneously during iteration. This eliminates the need to manually track indices with a separate counter variable.

Enumerate returns tuples containing (index, value) pairs, which you can unpack directly in your for loop. By default, enumeration starts at 0, but you can specify a different starting value if needed.

## Key Concepts

### Simultaneous Access to Index and Value

Without enumerate, accessing indices requires using range(len(sequence)) or maintaining a manual counter. Enumerate provides a cleaner, more Pythonic approach by yielding both the index and value in each iteration. This makes code more readable and less error-prone.

### Tuple Unpacking in Loops

Enumerate returns tuples, which you can unpack directly in the for statement: `for index, value in enumerate(iterable)`. The first variable receives the index, the second receives the value. This unpacking syntax is clean and expressive.

### Finding Positions

Enumerate is particularly useful when you need to know the position of elements while processing them. Common use cases include finding the index of specific values, processing elements based on their position, or building position-aware transformations.

## Example

```python
# Without enumerate - manual index tracking
fruits = ['apple', 'banana', 'cherry']
index = 0
for fruit in fruits:
    print(f"{index}: {fruit}")
    index += 1

# With enumerate - cleaner and more Pythonic
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output: 0: apple, 1: banana, 2: cherry

# Finding the index of a specific value
numbers = [10, 20, 30, 40, 50]
for i, num in enumerate(numbers):
    if num == 30:
        print(f"Found 30 at index {i}")

# Starting enumeration at a different number
for position, letter in enumerate('ABC', start=1):
    print(f"Position {position}: {letter}")
# Output: Position 1: A, Position 2: B, Position 3: C
```

## Your Task

You'll practice using enumerate() to iterate over sequences while accessing both indices and values, including finding specific elements and their positions.
