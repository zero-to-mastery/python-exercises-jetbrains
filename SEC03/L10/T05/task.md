# Variable Scope

## What You'll Learn

How Python resolves variable names using the LEGB rule: Local, Enclosing, Global, and Built-in scopes.

## Concept Overview

Variable scope determines where in your code a variable can be accessed. Python searches for variables in a specific order: Local scope (inside the current function), Enclosing scope (in outer functions), Global scope (module level), and Built-in scope (Python's built-in names). Understanding scope prevents naming conflicts and bugs.

## Key Concepts

### Local Scope

Variables defined inside a function exist only in that function's local scope. They're created when the function is called and destroyed when it returns. Local variables with the same name as outer variables shadow the outer ones within the function.

### Enclosing Scope

When you have nested functions, inner functions can access variables from their enclosing (outer) functions. These variables exist in the enclosing function's scope and are accessible to all nested functions within it.

### Global Scope

Variables defined at the module level (outside all functions) have global scope. They're accessible throughout the module. Functions can read global variables, but to modify them, you must use the global keyword.

## Example

```python
module_var = "I'm global"  # Global scope

def outer_function():
    outer_var = "I'm in enclosing scope"  # Enclosing scope

    def inner_function():
        inner_var = "I'm local"  # Local scope
        print(inner_var)  # Local
        print(outer_var)  # Enclosing
        print(module_var)  # Global
        print(len)  # Built-in

    inner_function()

outer_function()

# Scope resolution order
x = "global"

def test():
    x = "local"  # Shadows global x
    print(x)  # Prints "local"

test()
print(x)  # Prints "global"
```

## Your Task

You'll practice understanding variable scope by observing how Python resolves variable names in nested functions, distinguishing between local, enclosing, and global scopes.
