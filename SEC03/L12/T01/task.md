# First GUI

## What You'll Learn

Use nested loops and conditional logic to transform matrix data into visual ASCII art patterns.

## Concept Overview

This exercise combines nested loops, conditional statements, and matrix (2D list) manipulation to create visual patterns from data. You'll iterate through a two-dimensional list and convert numeric values into characters, demonstrating how data can be visualized through simple text representations.

This type of problem teaches fundamental skills: working with nested data structures, controlling output formatting, and thinking about how data maps to visual representations.

## Key Concepts

### Nested Loops for 2D Data

Process matrices using nested for loops:

```python
matrix = [[1, 0, 1], [0, 1, 0]]
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row
```

### Conditional Formatting

Transform values based on conditions:

```python
for value in data:
    if value == 1:
        print('*', end='')
    else:
        print(' ', end='')
```

### Output Control with end Parameter

Control print behavior to create patterns:

```python
print('*', end='')   # No newline
print('*', end=' ')  # Space separator
print('*')           # Newline (default)
```

### Data to Visual Mapping

Convert numeric data to visual representation:

```python
# 0 = space, 1 = asterisk
picture = [[0, 1, 0], [1, 1, 1]]
# Output:  *
#         ***
```

## Example

```python
# Create a simple pattern
grid = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

# Convert to ASCII art
for row in grid:
    for pixel in row:
        if pixel == 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()  # New line after each row

# Output creates a rectangle pattern
```

## Your Task

Practice using nested loops to process two-dimensional data and convert numeric values into visual ASCII art. Understand how to control output formatting and map data values to different characters to create patterns.
