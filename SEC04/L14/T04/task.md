# Super Function

## What You'll Learn

Use the `super()` function to call methods from parent classes, enabling proper initialization and method extension in inheritance hierarchies.

## Concept Overview

The `super()` function provides access to methods from a parent class, which is essential when you want to extend rather than completely replace parent functionality. It's most commonly used in `__init__` methods to ensure the parent class is properly initialized before adding child-specific initialization.

Using `super()` makes your code more maintainable and supports multiple inheritance correctly by following Python's Method Resolution Order (MRO).

## Key Concepts

### Calling Parent __init__

Initialize the parent class before adding child-specific attributes:

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent __init__
        self.age = age           # Add child attribute
```

### Extending Methods

Call parent method and add additional behavior:

```python
class Parent:
    def greet(self):
        return "Hello"

class Child(Parent):
    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting}, and welcome!"
```

### Why super() vs Direct Call

`super()` respects MRO in multiple inheritance:

```python
super().__init__()  # Recommended
ParentClass.__init__(self)  # Less flexible
```

## Example

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"Employee: {self.name}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Initialize parent
        self.department = department     # Add child attribute

    def describe(self):
        base = super().describe()  # Get parent description
        return f"{base}, Manager of {self.department}"

manager = Manager("Alice", 80000, "Engineering")
print(manager.describe())
# Output: Employee: Alice, Manager of Engineering
```

## Your Task

Practice using `super()` to call parent class methods, especially in initialization. Understand how it enables extending parent functionality rather than replacing it.
