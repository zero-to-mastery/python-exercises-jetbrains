# Map Filter Zip Reduce

## What You'll Learn

Use functional programming tools - map(), filter(), zip(), and reduce() - to process sequences efficiently with higher-order functions.

## Concept Overview

Functional programming emphasizes using functions as first-class objects. Python provides several built-in higher-order functions that accept functions as arguments and operate on sequences.

## Key Concepts

### map()

Apply a function to every item:

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))
```

### filter()

Select items that match a condition:

```python
evens = filter(lambda x: x % 2 == 0, numbers)
```

### zip()

Combine multiple sequences:

```python
names = ["Alice", "Bob"]
ages = [25, 30]
combined = zip(names, ages)
```

### reduce()

Accumulate values:

```python
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
```

## Example

```python
from functools import reduce

prices = [10.50, 25.00, 5.75, 30.25]
with_tax = list(map(lambda p: p * 1.08, prices))
expensive = list(filter(lambda p: p > 20, prices))
total = reduce(lambda x, y: x + y, prices)
```

## Your Task

Practice using map(), filter(), zip(), and reduce() to transform and process sequences efficiently.
