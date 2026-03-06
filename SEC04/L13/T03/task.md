# Init Method

## What You'll Learn

Use the `__init__` method to initialize objects with specific attributes when they're created.

## Concept Overview

The `__init__` method (initializer) is a special method that Python automatically calls when you create a new object. It allows you to set up the initial state of an object by assigning values to its attributes. This ensures every object starts with the data it needs.

The `__init__` method receives `self` as its first parameter, which refers to the instance being created, followed by any parameters you want to pass during instantiation.

## Key Concepts

### The __init__ Method

Define initialization logic that runs automatically:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)
```

### The self Parameter

`self` represents the instance being created. Use it to assign attributes:

```python
class Person:
    def __init__(self, name):
        self.name = name  # Assigns to this instance
```

### Initialization Parameters

Pass arguments during instantiation to customize each object:

```python
person1 = Person("Alice")
person2 = Person("Bob")
# Each has different name attribute
```

## Example

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Brave New World", "Aldous Huxley", 311)

print(book1.title)   # 1984
print(book2.author)  # Aldous Huxley
```

## Your Task

Explore how the `__init__` method initializes objects with custom data. Understand how `self` refers to the instance and how parameters become object attributes.
