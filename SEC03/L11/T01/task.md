# Docstrings

## What You'll Learn

Write documentation strings (docstrings) to document your functions, classes, and modules for better code maintainability and accessibility.

## Concept Overview

Docstrings are string literals that appear right after the definition of a function, method, class, or module. They serve as built-in documentation, explaining what the code does, its parameters, and return values. Unlike comments, docstrings are accessible at runtime through the `__doc__` attribute and can be used by documentation generation tools and the `help()` function.

Good docstrings make code self-documenting, helping other developers (and your future self) understand how to use your code without reading the implementation details.

## Key Concepts

### Function Docstrings

Place a string literal as the first statement in a function:

```python
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return 3.14159 * radius ** 2
```

### Multi-line Docstrings

For complex functions, use multi-line docstrings with detailed information:

```python
def divide(a, b):
    """
    Divide two numbers.
    
    Args:
        a: The dividend
        b: The divisor
    
    Returns:
        The quotient of a divided by b
    """
    return a / b
```

### Accessing Docstrings

Docstrings can be accessed programmatically:

```python
print(calculate_area.__doc__)  # Print docstring
help(calculate_area)            # Display formatted help
```

### Docstring Conventions

Follow PEP 257 conventions:
- Use triple quotes even for one-line docstrings
- First line should be a brief summary
- Separate summary from details with a blank line
- Describe parameters and return values

## Example

```python
def greet_user(name, greeting="Hello"):
    """
    Generate a personalized greeting.
    
    Args:
        name (str): The person's name
        greeting (str): The greeting word (default: "Hello")
    
    Returns:
        str: A formatted greeting message
    """
    return f"{greeting}, {name}!"

# Access the docstring
print(greet_user.__doc__)
help(greet_user)
```

## Your Task

Practice writing docstrings for functions to document their purpose and usage. Use the `help()` function and `__doc__` attribute to see how docstrings improve code readability and serve as inline documentation.
