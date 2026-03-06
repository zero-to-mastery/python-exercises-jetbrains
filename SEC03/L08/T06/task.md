# Loop Accumulation Pattern

## What You'll Learn

How to use loops with accumulator variables to compute aggregate values like sums, counts, or other cumulative results.

## Concept Overview

The accumulator pattern is a fundamental programming technique where you initialize a variable before a loop, then update it during each iteration to build up a result. This pattern is used to calculate sums, counts, products, concatenations, or any value that accumulates across multiple iterations.

Understanding this pattern is essential for data processing tasks where you need to combine or aggregate information from a collection. It's the foundation for many common operations before using built-in functions or more advanced techniques.

## Key Concepts

### Initialize Before the Loop

The accumulator variable must be initialized before the loop starts, typically to an appropriate starting value (0 for sums, 1 for products, empty string for concatenation, etc.). This starting value depends on what you're accumulating.

### Update During Each Iteration

Inside the loop, you update the accumulator based on the current element. For sums, you add the element to the accumulator. For counts, you increment by 1. For products, you multiply. The update operation depends on your goal.

### Use After the Loop

After the loop completes, the accumulator holds the final result. This result represents the aggregated value across all iterations. You can then use this value for further calculations, comparisons, or output.

## Example

```python
# Sum of numbers
numbers = [5, 12, 8, 3, 20]
total = 0  # Initialize accumulator
for num in numbers:
    total += num  # Update accumulator
print(total)  # 48

# Counting specific items
fruits = ['apple', 'banana', 'apple', 'cherry', 'apple']
apple_count = 0
for fruit in fruits:
    if fruit == 'apple':
        apple_count += 1
print(apple_count)  # 3

# Product of numbers
values = [2, 3, 4]
product = 1  # Start at 1 for multiplication
for value in values:
    product *= value
print(product)  # 24

# Concatenating strings
words = ['Hello', 'World', '!']
sentence = ''
for word in words:
    sentence += word + ' '
print(sentence.strip())  # Hello World !
```

## Your Task

You'll practice using the accumulator pattern to calculate the sum of numbers in a list by initializing a counter before the loop and updating it during each iteration.
