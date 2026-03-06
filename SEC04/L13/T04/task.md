# Attributes and Methods

## What You'll Learn

Define and use attributes (data) and methods (behavior) within classes to create objects with both state and functionality.

## Concept Overview

Classes encapsulate both data (attributes) and behavior (methods). Attributes are variables that belong to an object and store its state. Methods are functions that belong to an object and define its behavior. Together, they create objects that combine data with the operations that can be performed on that data.

This encapsulation is a core principle of OOP, allowing you to create self-contained objects that manage their own data and provide specific operations.

## Key Concepts

### Instance Attributes

Data unique to each instance, typically set in `__init__`:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute
```

### Instance Methods

Functions that operate on instance data, always receiving `self`:

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        return f"{self.brand} goes beep!"
```

### Accessing Attributes and Methods

Use dot notation to access both:

```python
my_car = Car("Toyota", "Camry")
print(my_car.brand)    # Access attribute
print(my_car.honk())   # Call method
```

## Example

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance

account = BankAccount("Alice", 1000)
print(account.owner)        # Alice
print(account.deposit(500)) # 1500
print(account.withdraw(200))# 1300
```

## Your Task

Practice defining classes with both attributes and methods. Understand how methods can access and modify instance attributes through `self`.
