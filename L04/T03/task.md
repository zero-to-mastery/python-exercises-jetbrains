In Python, a class can inherit from another class. This means the new class keeps the behavior of the parent class, but can also add or change some parts of it. Python even allows you to inherit from built-in classes such as `list`, `str`, and `dict`, so you can create your own version of a familiar type.

```python
class MyString(str):
    pass
````

Here, `MyString` still behaves like a normal string because it inherits from `str`.

A child class can also override a method from its parent class. This means replacing the original behavior with a new one.

```python
class LoudString(str):
    def lower(self):
        return "changed"
```
The `issubclass()` function is used to check whether one class inherits from another. It returns `True` if the first class is a child class of the second class, and `False` otherwise.

```python
issubclass(bool, int)
issubclass(str, list)
```

The first example returns `True`, while the second returns `False`.

This is useful when you want to check class relationships in Python’s inheritance hierarchy.