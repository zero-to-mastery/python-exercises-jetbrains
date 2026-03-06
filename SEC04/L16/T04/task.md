# Decorators

## What You'll Learn

Use decorators to modify or enhance functions without changing their source code.

## Concept Overview

Decorators are a powerful feature that allows you to wrap a function with another function, adding functionality before, after, or around the original function's execution.

## Key Concepts

### Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

### Decorators with Arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
```

## Example

```python
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@time_it
def slow_function(n):
    time.sleep(n)
    return "Done"

result = slow_function(2)
```

## Your Task

Explore decorators by creating functions that wrap other functions.
