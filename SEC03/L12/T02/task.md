# Tesla Exercise

## What You'll Learn

Refactor code into reusable functions with parameters and default values, understanding how function design improves code organization and reusability.

## Concept Overview

This exercise demonstrates the evolution of code from repetitive to reusable. You'll start with code that uses input() for user interaction, then refactor it into a function, and finally enhance it with parameters and default values. This progression shows why functions are essential for writing maintainable code.

The exercise specifically focuses on age validation logic, showing how wrapping code in a function allows it to be reused in different contexts and how parameters make functions flexible.

## Key Concepts

### Function Extraction

Convert repeated code into a reusable function:

```python
# Before: Repeated code
age = input("Age: ")
if int(age) < 18:
    print("Too young")
# ... repeat elsewhere ...

# After: Function
def check_age():
    age = input("Age: ")
    if int(age) < 18:
        print("Too young")

check_age()  # Reuse anywhere
```

### Parameters vs Input

Move from input() to parameters for flexibility:

```python
# Using input (less flexible)
def check_age():
    age = input("Age: ")
    process(age)

# Using parameters (more flexible)
def check_age(age):
    process(age)

check_age(25)  # Can be called with any value
```

### Default Parameter Values

Provide sensible defaults:

```python
def check_age(age=0):
    if age < 18:
        print("Too young")
    elif age >= 18:
        print("Allowed")

check_age()    # Uses default: 0
check_age(25)  # Uses provided: 25
```

### Function Benefits

Why functions improve code:
- Reusability: Write once, use many times
- Testability: Easier to test with parameters
- Maintainability: Fix bugs in one place
- Readability: Clear, named operations

## Example

```python
# Version 1: Hardcoded with input
def check_password():
    pwd = input("Password: ")
    if len(pwd) < 8:
        print("Too short")
    else:
        print("Valid")

# Version 2: With parameters
def check_password(password):
    if len(password) < 8:
        print("Too short")
    else:
        print("Valid")

# Version 3: With default and return value
def check_password(password="", min_length=8):
    return len(password) >= min_length

# Usage
result = check_password("secure123")
print("Valid" if result else "Invalid")
```

## Your Task

Practice refactoring code from using input() to using function parameters. Understand how parameters make functions more flexible and reusable, and how default values provide sensible fallbacks. Learn the progression from hardcoded values to parameterized, reusable functions.
