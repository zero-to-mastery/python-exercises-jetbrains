# Pets Everywhere

## What You'll Learn

Build upon OOP fundamentals by creating more complex classes with additional attributes and methods, reinforcing object-oriented design patterns.

## Concept Overview

This exercise extends your OOP practice with more sophisticated class design. You'll work with classes that have multiple attributes, various methods, and demonstrate how objects encapsulate both state (data) and behavior (methods) to model real-world entities more completely.

Practice is essential for mastering OOP. This exercise challenges you to think about how to organize data and functionality within a class structure.

## Key Concepts

### Rich Object Models

Create objects with multiple attributes that fully describe an entity:

```python
class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
```

### Multiple Methods

Provide various behaviors through different methods:

```python
class Vehicle:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

    def describe(self):
        return f"{self.year} {self.make} {self.model}"
```

### Object Interaction

Objects can be used together and passed to functions:

```python
def compare_ages(pet1, pet2):
    return pet1.age > pet2.age
```

## Example

```python
class Restaurant:
    def __init__(self, name, cuisine, rating):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.is_open = False

    def open(self):
        self.is_open = True
        return f"{self.name} is now open"

    def close(self):
        self.is_open = False
        return f"{self.name} is now closed"

    def describe(self):
        status = "open" if self.is_open else "closed"
        return f"{self.name} ({self.cuisine}) - {self.rating} stars - {status}"

restaurant = Restaurant("Luigi's", "Italian", 4.5)
print(restaurant.open())
print(restaurant.describe())
```

## Your Task

Design and implement a class with multiple attributes and methods. Create several instances and interact with them to practice OOP design patterns.
