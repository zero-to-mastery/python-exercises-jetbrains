# *args and **kwargs

## What You'll Learn

How to use *args and **kwargs to accept variable numbers of positional and keyword arguments in functions.

## Concept Overview

*args and **kwargs allow functions to accept flexible numbers of arguments. *args collects extra positional arguments into a tuple, while **kwargs collects extra keyword arguments into a dictionary. This enables functions to handle varying numbers of inputs without defining every parameter explicitly.

## Key Concepts

### * args for Variable Positional Arguments

The *args parameter collects any extra positional arguments into a tuple. You can iterate over args or use it like any tuple. The name 'args' is conventional but you can use any name after the asterisk.

### **kwargs for Variable Keyword Arguments

The **kwargs parameter collects extra keyword arguments into a dictionary. Keys are parameter names, values are the arguments passed. You can access kwargs like any dictionary, iterating over keys, values, or items.

### Parameter Order Rules

Parameters must follow a specific order: regular parameters, *args, default parameters, **kwargs. This order ensures Python can correctly match arguments to parameters during function calls.

## Example

```python
def flexible_function(required, *args, default='hi', **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

flexible_function('必須', 1, 2, 3, default='hello', key1='value1', key2='value2')

# Summing with *args
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15

# Processing with **kwargs
def process_data(**data):
    total = 0
    for key, value in data.items():
        print(f"{key}: {value}")
        if isinstance(value, (int, float)):
            total += value
    return total

print(process_data(a=5, b=10, c=15))  # 30
```

## Your Task

You'll practice using *args to accept variable positional arguments and **kwargs to accept variable keyword arguments, following the correct parameter ordering rules.
