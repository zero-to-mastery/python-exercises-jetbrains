# Multiple Inheritance

## What You'll Learn

Understand multiple inheritance, where a class can inherit from more than one parent class, combining features from multiple sources.

## Concept Overview

Multiple inheritance allows a class to inherit attributes and methods from multiple parent classes. This can be powerful for combining functionality from different sources, but requires careful design to avoid complexity and ambiguity.

Python handles multiple inheritance through its Method Resolution Order (MRO), which determines the order in which parent classes are searched for methods.

## Key Concepts

### Inheriting from Multiple Parents

Specify multiple parent classes in parentheses:

```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()   # From Flyable
duck.swim()  # From Swimmable
```

### Method Resolution Order (MRO)

Python searches classes left-to-right, depth-first:

```python
class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"

class C(A, B):
    pass

c = C()
c.method()  # Returns "A" (A comes before B in MRO)
```

### Diamond Problem

When multiple inheritance paths exist to the same parent:

```python
class Animal:
    def eat(self):
        return "Eating"

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Bat(Mammal, Bird):
    pass  # MRO handles the diamond
```

## Example

```python
class Engine:
    def start_engine(self):
        return "Engine started"

class Electronics:
    def turn_on_display(self):
        return "Display on"

class GPS:
    def get_location(self):
        return "Location: 40.7128° N, 74.0060° W"

class SmartCar(Engine, Electronics, GPS):
    def __init__(self, model):
        self.model = model

    def start(self):
        results = []
        results.append(self.start_engine())
        results.append(self.turn_on_display())
        results.append(self.get_location())
        return " | ".join(results)

car = SmartCar("Tesla Model 3")
print(car.start())
# Engine started | Display on | Location: 40.7128° N, 74.0060° W
```

## Your Task

Explore multiple inheritance by creating classes that inherit from multiple parents. Understand how Python combines functionality from different sources.
