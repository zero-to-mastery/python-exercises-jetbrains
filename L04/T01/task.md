# Classes and Instances

A class is a way to describe a group of similar objects. It defines what data these objects should have when they are created. An object created from a class is called an **instance**. This means you can use one class to create many separate objects, and each of them can store its own values.

```python
class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

In this example, `Dog` is a class. The `__init__()` method is used to give each new object its own data. The `self` keyword refers to the current object, so `self.name` and `self.age` become attributes of that specific instance. The `species` value is a class attribute, which means it is shared by all objects created from the class.

To create an instance, call the class and pass the required values:

```python
dog1 = Dog('Buddy', 3)
dog2 = Dog('Max', 5)
```

These are two different instances of the same class. Even though they come from the same blueprint, they can store different names and ages.

You can access object attributes using dot notation:

```python
dog1.age
dog2.name
```

You can also use regular functions together with object attributes. For example, if you want to compare ages, you can pass them to a function and return the largest value.

```python
def get_largest(*args):
    return max(args)
```

In this task, you will create several instances of a class, access their age attributes, and find the largest age.
