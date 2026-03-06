# Extending List

## What You'll Learn

Create custom classes that inherit from built-in Python types like list, extending their functionality with custom methods.

## Concept Overview

Python's built-in types (list, dict, str, etc.) can be inherited and extended just like custom classes. This allows you to create specialized versions of built-in types that include additional functionality while maintaining all the original features.

## Key Concepts

### Inheriting from Built-in Types

Create a subclass of list:

```python
class MyList(list):
    pass

my_list = MyList([1, 2, 3])
my_list.append(4)
```

### Adding Custom Methods

```python
class MyList(list):
    def sum_all(self):
        return sum(self)
```

## Example

```python
class UniqueList(list):
    def append(self, item):
        if item not in self:
            super().append(item)
```

## Your Task

Practice creating custom classes that inherit from Python list type.
