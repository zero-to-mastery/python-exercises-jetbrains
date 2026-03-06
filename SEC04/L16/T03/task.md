# Comprehensions

## What You'll Learn

Use list, dictionary, and set comprehensions to create collections concisely using compact, readable syntax.

## Concept Overview

Comprehensions provide a concise way to create lists, dictionaries, and sets from existing sequences. They're often more efficient and pythonic than equivalent for loops.

## Key Concepts

### List Comprehensions

```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
```

### Comprehensions with Conditionals

```python
evens = [x for x in numbers if x % 2 == 0]
```

### Dictionary Comprehensions

```python
squares = {x: x**2 for x in range(5)}
```

### Set Comprehensions

```python
unique_squared = {x**2 for x in [1, 2, 2, 3, 3]}
```

## Example

```python
words = ["hello", "world", "python"]
uppercase = [w.upper() for w in words]
word_lengths = {word: len(word) for word in words}

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]

prices = [10.50, 25.00, 5.75, 30.25, 15.00]
expensive_with_tax = [
    round(price * 1.08, 2)
    for price in prices
    if price > 15
]
```

## Your Task

Practice writing list, dictionary, and set comprehensions to combine iteration, transformation, and filtering.
