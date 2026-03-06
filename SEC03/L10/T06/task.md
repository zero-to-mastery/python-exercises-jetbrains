# The global Keyword

## What You'll Learn

How to use the global keyword to modify global variables from within functions.

## Concept Overview

By default, assignment statements inside functions create new local variables rather than modifying global ones. The global keyword tells Python that you want to modify a variable in the global scope instead of creating a new local variable. This is necessary when functions need to update module-level state.

While global variables can be read from anywhere, modifying them requires explicit declaration with the global keyword. This design prevents accidental modification of global state and makes it clear when a function has side effects beyond its local scope.

## Key Concepts

### Reading vs Modifying Globals

Functions can read global variables without any special syntax. However, if you try to assign to a variable name inside a function, Python creates a new local variable by default. To modify the global variable instead, you must declare it global before assignment.

### The global Declaration

Place the global keyword before the variable name at the beginning of the function. This tells Python to use the global scope version of that variable for all references within the function. Multiple variables can be declared global in one statement or separately.

### Side Effects and Design

Using global variables can make code harder to understand and test because functions have side effects beyond their return values. It's generally better to pass values as parameters and return results. Use global sparingly, typically for configuration or application-wide state.

## Example

```python
counter = 0  # Global variable

def increment():
    global counter  # Declare we're using global counter
    counter += 1  # Modifies the global variable
    return counter

def read_counter():
    return counter  # Can read without global keyword

print(increment())  # 1
print(increment())  # 2
print(read_counter())  # 2

# Without global keyword
value = 10

def try_modify():
    value = 20  # Creates new local variable
    print(f"Inside function: {value}")

try_modify()  # Inside function: 20
print(f"Outside function: {value}")  # Outside function: 10 (unchanged)
```

## Your Task

You'll practice using the global keyword to modify global variables from within functions, observing how it differs from reading global variables or creating local ones.
