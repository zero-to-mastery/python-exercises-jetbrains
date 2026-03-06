# Class and Static Methods

## What You'll Learn

Differentiate between instance methods, class methods, and static methods, and understand when to use each type.

## Concept Overview

Python classes support three types of methods: instance methods (operate on instances), class methods (operate on the class itself), and static methods (utility functions that don't need access to instance or class data). Each serves a different purpose in object-oriented design.

Class methods are useful for alternative constructors or operations that affect the entire class. Static methods are utility functions related to the class but don't need access to class or instance data.

## Key Concepts

### Instance Methods

Regular methods that receive `self` and operate on instances:

```python
class MyClass:
    def instance_method(self):
        return f"Instance: {self}"
```

### Class Methods

Decorated with `@classmethod`, receive `cls` instead of `self`:

```python
class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
```

### Static Methods

Decorated with `@staticmethod`, don't receive `self` or `cls`:

```python
class MyClass:
    @staticmethod
    def utility_function(x, y):
        return x + y
```

## Example

```python
class Pizza:
    size = "medium"  # Class attribute

    def __init__(self, toppings):
        self.toppings = toppings  # Instance attribute

    @classmethod
    def change_default_size(cls, new_size):
        cls.size = new_size

    @staticmethod
    def is_valid_topping(topping):
        valid = ["cheese", "pepperoni", "mushrooms"]
        return topping in valid

# Instance method
pizza = Pizza(["cheese"])

# Class method - affects all instances
Pizza.change_default_size("large")

# Static method - utility function
print(Pizza.is_valid_topping("cheese"))  # True
```

## Your Task

Explore the three types of methods in Python classes. Understand when to use instance methods (for instance-specific operations), class methods (for class-level operations), and static methods (for utilities).
