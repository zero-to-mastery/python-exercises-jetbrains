# Inheritance

## What You'll Learn

Use inheritance to create new classes based on existing ones, promoting code reuse and establishing hierarchical relationships between classes.

## Concept Overview

Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass). This enables code reuse and creates hierarchical relationships where specialized classes extend the functionality of more general classes.

Inheritance models "is-a" relationships: a Dog is an Animal, a Manager is an Employee. This makes code more organized and reduces duplication.

## Key Concepts

### Basic Inheritance

Create a child class that inherits from a parent:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass  # Inherits speak() from Animal

dog = Dog()
print(dog.speak())  # "Some sound"
```

### Method Overriding

Child classes can override parent methods:

```python
class Dog(Animal):
    def speak(self):
        return "Woof!"  # Overrides parent's speak()
```

### Extending Functionality

Child classes add new methods while keeping inherited ones:

```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def fetch(self):  # New method
        return "Fetching ball"
```

## Example

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is starting"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def honk(self):
        return "Beep beep!"

class Motorcycle(Vehicle):
    def wheelie(self):
        return "Doing a wheelie!"

car = Car("Toyota", 4)
print(car.start())  # Inherited from Vehicle
print(car.honk())   # Car-specific method

bike = Motorcycle("Harley")
print(bike.start())   # Inherited from Vehicle
print(bike.wheelie()) # Motorcycle-specific method
```

## Your Task

Explore inheritance by creating parent and child classes. Observe how child classes inherit parent functionality while adding their own specialized behavior.
