# Polymorphism

## What You'll Learn

Understand polymorphism, which allows objects of different classes to be treated uniformly through a common interface while each implements behavior in its own way.

## Concept Overview

Polymorphism (meaning "many forms") allows different classes to implement the same method name in their own way. This enables you to write code that works with objects of different types as long as they share a common interface, making code more flexible and extensible.

Polymorphism is powerful because it lets you write generic code that operates on different types without knowing their specific implementations.

## Key Concepts

### Same Method, Different Behavior

Different classes implement the same method differently:

```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

# Both respond to speak(), but differently
```

### Treating Objects Uniformly

Write code that works with any object having the required method:

```python
def make_sound(animal):
    print(animal.speak())  # Works with any class that has speak()

make_sound(Cat())  # Meow
make_sound(Dog())  # Woof
```

### Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck" - Python doesn't care about the type, only that the method exists:

```python
class Robot:
    def speak(self):
        return "Beep boop"

make_sound(Robot())  # Works too!
```

## Example

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Polymorphic function - works with any shape
def print_area(shape):
    print(f"Area: {shape.area()}")

shapes = [Rectangle(5, 10), Circle(7), Triangle(4, 6)]
for shape in shapes:
    print_area(shape)  # Calls appropriate area() for each
```

## Your Task

Explore polymorphism by creating different classes that implement the same methods. Understand how this enables writing flexible code that works with various types.
