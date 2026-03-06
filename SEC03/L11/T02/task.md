# Clean Code

## What You'll Learn

Write clean, readable, and maintainable Python code following best practices and naming conventions.

## Concept Overview

Clean code is code that is easy to read, understand, and modify. It follows consistent naming conventions, uses meaningful variable names, avoids unnecessary complexity, and is well-organized. Writing clean code is crucial for long-term maintainability and collaboration with other developers.

Python has established conventions (PEP 8) that guide developers toward writing consistent, readable code. Following these conventions makes your code more professional and easier for others to work with.

## Key Concepts

### Meaningful Names

Use descriptive names that clearly indicate purpose:

```python
# Poor
x = 86400
d = x / 3600

# Good
seconds_per_day = 86400
hours = seconds_per_day / 3600
```

### Naming Conventions

Python naming standards:
- Variables and functions: `lowercase_with_underscores`
- Classes: `CapitalizedWords`
- Constants: `UPPERCASE_WITH_UNDERSCORES`

### Simple and Direct

Write straightforward code:

```python
# Simple and clean
def is_even(number):
    return number % 2 == 0

# Clear boolean check
if is_even(value):
    process_even_number()
```

### Single Responsibility

Functions should do one thing well:

```python
def calculate_total(items):
    return sum(items)

def apply_discount(total, percent):
    return total * (1 - percent / 100)

# Each function has a single, clear purpose
```

## Example

```python
# Clean code example
MAX_LOGIN_ATTEMPTS = 3

def is_valid_password(password):
    """Check if password meets minimum requirements."""
    minimum_length = 8
    return len(password) >= minimum_length

def authenticate_user(username, password):
    """Authenticate user with credentials."""
    if not is_valid_password(password):
        return False
    # Authentication logic here
    return True

# Usage
result = authenticate_user("alice", "secure123")
```

## Your Task

Study examples of clean code practices including meaningful naming, proper formatting, and code organization. Learn to write code that clearly communicates its intent and follows Python conventions.
