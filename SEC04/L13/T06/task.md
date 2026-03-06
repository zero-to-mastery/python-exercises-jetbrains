# Cats Everywhere

## What You'll Learn

Apply OOP concepts by creating a class with attributes and methods, and instantiating multiple objects with different characteristics.

## Concept Overview

This exercise brings together the fundamental OOP concepts you've learned: defining classes, using `__init__` for initialization, setting instance attributes, and creating methods. By building a practical example, you'll solidify your understanding of how classes model real-world entities.

Creating multiple instances from a single class demonstrates how OOP enables code reuse and organization by defining a blueprint once and creating many objects from it.

## Key Concepts

### Complete Class Definition

Combine all OOP elements into a functional class:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f"{self.name} makes a sound"
```

### Multiple Instances with Different Data

Create various objects with unique characteristics:

```python
animal1 = Animal("Leo", "Lion")
animal2 = Animal("Tweety", "Bird")
```

### Method Calls on Different Instances

Each instance responds based on its own data:

```python
print(animal1.make_sound())  # Leo makes a sound
print(animal2.make_sound())  # Tweety makes a sound
```

## Example

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, subject):
        return f"{self.name} is studying {subject}"

    def get_grade(self):
        return f"{self.name}'s grade: {self.grade}"

alice = Student("Alice", "A")
bob = Student("Bob", "B")

print(alice.study("Math"))     # Alice is studying Math
print(bob.get_grade())         # Bob's grade: B
```

## Your Task

Create a complete class with initialization, attributes, and methods. Instantiate multiple objects and call methods on each to see how they maintain independent state while sharing behavior.
