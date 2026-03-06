# Generators Exercise

## What You'll Learn

Apply generator concepts to solve practical problems efficiently.

## Concept Overview

This exercise challenges you to use generators in realistic scenarios. Generators excel at processing large datasets and creating infinite sequences.

## Key Concepts

### Practical Generator Patterns

- Reading large files line by line
- Processing infinite sequences
- Implementing data pipelines
- Filtering and transforming streams

### Memory Efficiency

```python
def get_lines(file):
    for line in open(file):
        yield line
```

### Generator Composition

```python
def process(data_gen):
    for item in data_gen:
        yield transform(item)
```

## Example

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(n, gen):
    for _ in range(n):
        yield next(gen)

def even_fibonacci(n):
    fib = fibonacci()
    evens = (x for x in fib if x % 2 == 0)
    return list(take(n, evens))

print(even_fibonacci(5))
```

## Your Task

Practice using generators to solve problems efficiently with lazy evaluation.
