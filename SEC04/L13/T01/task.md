# OOP Introduction

## What You'll Learn

Understand the fundamentals of Object-Oriented Programming (OOP) in Python, including how to create classes, instantiate objects, and explore Python's type system.

## Concept Overview

Object-Oriented Programming is a programming paradigm that organizes code around objects rather than functions and logic. In Python, everything is an object - numbers, strings, lists, and even functions. Understanding OOP allows you to create custom data types (classes) that bundle data and functionality together, making code more modular, reusable, and easier to maintain.

A class serves as a blueprint for creating objects (instances). Each object created from a class can have its own data while sharing the same structure and behavior defined by the class.

## Key Concepts

### Classes and Objects

A class is a template that defines the structure and behavior for objects. You create a class using the `class` keyword. An object is an instance of a class - a concrete realization of the class blueprint.

```python
class Car:
    pass

my_car = Car()  # Create an object (instance) of Car
```

### The type() Function

Everything in Python has a type. The `type()` function reveals what type an object is. Built-in types include `int`, `str`, `list`, `dict`, etc. When you create a class, you're creating a new type.

```python
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
```

### Creating Multiple Instances

You can create multiple objects from the same class. Each object is independent - they share the same class structure but are separate entities in memory.

```python
car1 = Car()
car2 = Car()
# car1 and car2 are different objects
```

## Example

```python
# Define a custom class
class Book:
    pass

# Create instances
book1 = Book()
book2 = Book()
book3 = Book()

# Check their types
print(type(book1))  # <class '__main__.Book'>

# They're different objects
print(book1 == book2)  # False
print(book1 is book2)  # False
```

## Your Task

Explore the basics of OOP by creating a simple class and instantiating multiple objects from it. Use the `type()` function to examine how Python represents both built-in types and custom classes.
