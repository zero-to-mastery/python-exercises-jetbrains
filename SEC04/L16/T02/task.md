# Lambda Functions

## What You'll Learn

Create anonymous functions using lambda expressions for simple, one-line function definitions.

## Concept Overview

Lambda functions are small, anonymous functions defined with the lambda keyword. They're useful for short, simple operations that don't need a full function definition.

## Key Concepts

### Lambda Syntax

```python
add = lambda x, y: x + y
```

### Lambda with Higher-Order Functions

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
evens = filter(lambda x: x % 2 == 0, numbers)
```

### Lambda as Arguments

```python
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
```

## Example

```python
square = lambda x: x ** 2
print(square(5))

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92}
]
by_grade = sorted(students, key=lambda s: s['grade'], reverse=True)
```

## Your Task

Practice creating and using lambda functions for simple operations.
