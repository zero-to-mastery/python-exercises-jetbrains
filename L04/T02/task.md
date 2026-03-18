# Inheritance and Object Lists

Inheritance lets one class use the behavior of another class. A new class can inherit attributes and methods from an existing class, and also add its own methods.

```python
class Animal:
    def move(self):
        return "moving"


class Dog(Animal):
    def bark(self):
        return "woof"
```

Here, `Dog` inherits from `Animal`. This means a `Dog` instance can use the `move()` method even though it is defined in the parent class.

```python
dog = Dog()
dog.move()
```

A class can also work with a list of objects. This is useful when you want to perform the same action for many instances.

```python
class Group:
    def __init__(self, items):
        self.items = items

    def show_moves(self):
        result = []
        for item in self.items:
            result.append(item.move())
        return result
```

In this example, the `Group` class stores several objects and calls the same method on each of them. This works because every object in the list has a `move()` method.

In this task, you will create several instances from child classes, put them into a list, create an object that stores this list, and call a method for all of them.
