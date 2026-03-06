# Dunder Methods

## What You'll Learn

Understand and implement dunder methods (double underscore methods) to customize how your objects behave with Python's built-in operations.

## Concept Overview

Dunder methods (also called magic methods or special methods) are methods with names starting and ending with double underscores, like `__init__`, `__str__`, or `__add__`. They allow your custom classes to integrate with Python's built-in operations like printing, arithmetic, comparisons, and more.

By implementing these methods, you make your objects behave like built-in types, providing a more intuitive and pythonic interface.

## Key Concepts

### String Representation

Control how objects are displayed:

```python
class Book:
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f"Book: {self.title}"
```

### Arithmetic Operations

Enable math operations on your objects:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

### Comparison Operations

Implement comparison logic:

```python
class Person:
    def __init__(self, age):
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age
```

## Example

```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __str__(self):
        return f"${self.amount:.2f}"
    
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __eq__(self, other):
        return self.amount == other.amount

wallet = Money(100)
item = Money(25)
print(wallet)        # $100.00
print(wallet - item) # $75.00
print(wallet > item) # True
```

## Your Task

Explore dunder methods that customize object behavior. Implement methods like `__str__`, `__add__`, and `__eq__` to make your objects work seamlessly with Python's built-in operations.
