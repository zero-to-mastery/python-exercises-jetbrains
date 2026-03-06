# Return Statements

## What You'll Learn

How to use return statements to send values back from functions and use those returned values in expressions or other functions.

## Concept Overview

The return statement makes functions produce output values that can be used elsewhere in your program. When a function executes a return statement, it immediately exits and sends the specified value back to wherever the function was called. This value can be assigned to a variable, used in expressions, or passed to other functions.

Without a return statement, functions return None by default. Understanding return values is crucial because it's how functions communicate their results to the rest of your program, enabling function composition and data processing pipelines.

## Key Concepts

### Return Values

The return keyword is followed by an expression whose value becomes the function's output. When Python encounters return, it evaluates the expression, exits the function immediately, and provides that value to the caller. Any code after the return statement in that code path won't execute.

### Using Returned Values

Returned values can be assigned to variables, printed, used in calculations, or passed as arguments to other functions. This enables you to chain function calls together, where one function's output becomes another's input. This pattern is fundamental to building complex programs from simple functions.

### Nested Functions

Functions can be defined inside other functions. The inner function has access to the outer function's variables. When you return a value from a nested function, that value passes through the outer function's return statement. This pattern is useful for organizing related functionality and creating closures.

## Example

```python
# Basic return
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Using returned value in expression
total = add(10, 20) + add(5, 15)
print(total)  # 50

# Returning to another function
def multiply(x, y):
    return x * y

def calculate(a, b, c):
    sum_result = add(a, b)
    return multiply(sum_result, c)

print(calculate(2, 3, 4))  # (2+3)*4 = 20

# Nested function
def outer(x, y):
    def inner(a, b):
        return a * b
    return inner(x, y) + 10

print(outer(3, 4))  # 3*4 + 10 = 22

# Multiple returns based on condition
def absolute_value(num):
    if num < 0:
        return -num
    return num  # Only executes if num >= 0
```

## Your Task

You'll practice using return statements to send values back from functions, assigning returned values to variables, and composing functions by passing returned values to other functions, including nested function scenarios.
