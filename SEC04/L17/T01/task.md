# Generator Basics

## What You'll Learn

Understand generators - functions that yield values one at a time instead of returning all values at once.

## Concept Overview

Generators are functions that produce a sequence of values over time using the yield keyword. They generate values on-demand (lazily), making them memory-efficient for large datasets.

## Key Concepts

### Generator Functions

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)
```

### Lazy Evaluation

```python
def big_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

### Generator Expressions

```python
squares = (x**2 for x in range(10))
```

## Example

```python
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(10):
    print(num)

even_squares = (x**2 for x in range(100) if x % 2 == 0)
print(next(even_squares))
```

## Your Task

Practice creating generator functions using yield for memory-efficient iteration.
