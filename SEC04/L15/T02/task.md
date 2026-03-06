# Object Introspection

## What You'll Learn

Use Python's introspection tools to examine objects at runtime, discovering their attributes, methods, and types dynamically.

## Concept Overview

Introspection is Python's ability to examine objects at runtime to determine their type, attributes, methods, and other properties. This is powerful for debugging, building generic tools, and understanding code behavior dynamically.

## Key Concepts

### Type and Class Information

Determine an object's type:

```python
x = [1, 2, 3]
print(type(x))
print(isinstance(x, list))
```

### Attribute Discovery

List all attributes and methods:

```python
print(dir(x))
print(hasattr(x, 'append'))
print(getattr(x, 'append'))
```

## Example

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Alice")
print(type(person))
print(hasattr(person, 'name'))
print(callable(person.greet))
```

## Your Task

Practice using Python's introspection tools to examine objects dynamically. Use type(), dir(), hasattr(), getattr(), and isinstance() to explore object properties at runtime.
