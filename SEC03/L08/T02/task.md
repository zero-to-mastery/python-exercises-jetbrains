# The range() Function

## What You'll Learn

How to use the range() function to generate sequences of numbers for loop iteration with different start, stop, and step values.

## Concept Overview

The `range()` function generates a sequence of numbers, which is particularly useful for repeating actions a specific number of times or generating numeric sequences. Range is memory-efficient because it doesn't create a list of all numbers upfront; instead, it generates numbers on-demand.

Range can be used with one, two, or three arguments: `range(stop)`, `range(start, stop)`, or `range(start, stop, step)`. Understanding these variations allows you to create any arithmetic sequence you need for iteration.

## Key Concepts

### Range with Single Argument

When called with one argument, `range(n)` generates numbers from 0 up to (but not including) n. This is the most common use case for repeating an action n times. The sequence always starts at 0 by default.

### Range with Start and Stop

With two arguments, `range(start, stop)` generates numbers from start up to (but not including) stop. This allows you to control where the sequence begins and ends. The stop value is never included in the sequence.

### Range with Step

The third argument specifies the step size between numbers. A positive step counts upward, while a negative step counts downward. For countdown loops, you need start > stop with a negative step. If the step would never reach stop, range generates an empty sequence.

## Example

```python
# Single argument: 0 to n-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Two arguments: start to stop-1
for i in range(5, 10):
    print(i)  # 5, 6, 7, 8, 9

# With step: every other number
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Countdown with negative step
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1

# Converting to list to see all values
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

# Using underscore when you don't need the value
for _ in range(3):
    print("Hello")  # Prints Hello three times
```

## Your Task

You'll practice using range() with different argument combinations to generate various numeric sequences for loop iteration, including forward sequences, backward sequences, and sequences with custom steps.
