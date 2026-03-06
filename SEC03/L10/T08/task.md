# Finding Maximum Even Number

## What You'll Learn

How to apply function concepts, loops, and conditional logic to filter and find specific values in a list.

## Concept Overview

This exercise combines several programming concepts: defining functions with parameters, iterating over lists, filtering elements based on conditions, and finding maximum values. The problem requires you to identify even numbers from a list and determine which is the highest.

This type of data processing task is common in real programs. It teaches you to break down problems into steps: filter the data based on criteria, then apply an aggregate operation to the filtered results.

## Key Concepts

### Filtering with Conditionals

To find even numbers, you check if each number is divisible by 2 using the modulo operator (%). If `num % 2 == 0`, the number is even. You collect these numbers for further processing. The `not` operator can also be used with the modulo result since 0 is falsy.

### Collecting Results

As you iterate through the list, you build a new collection containing only the elements that meet your criteria. This filtered collection becomes the input for the next operation. You can use a list to accumulate matching values.

### Finding Maximum Values

Once you have the filtered list of even numbers, you find the maximum using Python's `max()` function. This built-in function returns the largest value from an iterable. Alternatively, you could track the maximum manually during iteration.

## Example

```python
def find_max_even(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return max(evens) if evens else None

print(find_max_even([1, 2, 3, 4, 5, 6]))  # 6
print(find_max_even([10, 15, 20, 25, 30]))  # 30
print(find_max_even([1, 3, 5, 7]))  # None

# Alternative: track max during iteration
def find_max_even_v2(numbers):
    max_even = None
    for num in numbers:
        if num % 2 == 0:
            if max_even is None or num > max_even:
                max_even = num
    return max_even

print(find_max_even_v2([7, 12, 3, 18, 9]))  # 18
```

## Your Task

You'll practice writing a function that filters a list to find even numbers and returns the highest even number found, combining iteration, conditional logic, and aggregation concepts.
