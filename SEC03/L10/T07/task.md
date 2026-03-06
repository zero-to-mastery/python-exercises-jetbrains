# The nonlocal Keyword

## What You'll Learn

How to use the nonlocal keyword to modify variables in enclosing function scopes from nested functions.

## Concept Overview

The nonlocal keyword works similarly to global, but for enclosing function scopes rather than the module-level scope. When you have nested functions and want the inner function to modify a variable from the outer function, you use nonlocal. Without it, assignment creates a new local variable in the inner function.

This is particularly useful for closures and maintaining state across multiple calls to inner functions. It allows inner functions to update variables in their enclosing scope while keeping those variables private from the global scope.

## Key Concepts

### Enclosing Scope Modification

Inner functions can read variables from enclosing functions without special syntax. However, assigning to those variables creates new local variables by default. The nonlocal keyword tells Python to modify the enclosing scope's variable instead.

### nonlocal vs global

While global refers to module-level variables, nonlocal refers to variables in the nearest enclosing function scope. Use nonlocal when working with nested functions and you need to modify the outer function's variables. Use global for module-level variables.

### Closure Applications

The nonlocal keyword is essential for creating closures that maintain and modify state. This pattern allows you to create functions with private state that persists across calls, without using global variables or class instances.

## Example

```python
def counter():
    count = 0  # Enclosing scope variable

    def increment():
        nonlocal count  # Modify enclosing scope
        count += 1
        return count

    def reset():
        nonlocal count
        count = 0

    return increment, reset

inc, rst = counter()
print(inc())  # 1
print(inc())  # 2
print(inc())  # 3
rst()
print(inc())  # 1

# Without nonlocal
def outer():
    x = "outer value"

    def inner():
        x = "inner value"  # Creates new local variable
        print(f"Inner: {x}")

    inner()
    print(f"Outer: {x}")  # Still "outer value"

outer()
```

## Your Task

You'll practice using the nonlocal keyword to modify enclosing scope variables from nested functions, observing how it enables inner functions to update outer function state.
