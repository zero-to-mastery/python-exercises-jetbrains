# Creating Objects

## What You'll Learn

Instantiate objects from classes and understand the relationship between classes as blueprints and objects as instances.

## Concept Overview

In Object-Oriented Programming, a class serves as a blueprint or template that defines the structure and behavior of objects. Creating an object (instantiation) means creating a concrete instance based on that blueprint. Each object created from the same class shares the same structure but maintains its own independent state.

Understanding object instantiation is fundamental to OOP, as it allows you to create multiple instances with shared behavior but separate data.

## Key Concepts

### Object Instantiation

Create an object by calling the class name followed by parentheses:

```python
class Player:
    pass

player1 = Player()  # Creates first instance
player2 = Player()  # Creates second instance
```

### Independent Instances

Each object is independent - they're separate entities in memory:

```python
class Counter:
    pass

c1 = Counter()
c2 = Counter()

print(c1 is c2)  # False - different objects
```

### Class as a Callable

When you call a class like `Player()`, Python creates a new object and returns it. The class acts as a factory for creating instances.

## Example

```python
class Robot:
    pass

# Create multiple robot instances
robot_a = Robot()
robot_b = Robot()
robot_c = Robot()

# Each is a unique object
print(type(robot_a))  # <class '__main__.Robot'>
print(robot_a == robot_b)  # False
print(id(robot_a) == id(robot_b))  # False
```

## Your Task

Practice creating multiple objects from a class definition. Observe how each instance is independent while sharing the same class structure.
