# Function Parameters and Arguments

## What You'll Learn

How to define functions with parameters to accept input values and call them with arguments, including positional, default, and keyword arguments.

## Concept Overview

Parameters make functions flexible by allowing them to accept different input values each time they're called. Parameters are variables listed in the function definition, while arguments are the actual values passed when calling the function. This distinction is key to understanding function behavior.

Python supports several types of parameters: positional parameters (order matters), default parameters (have preset values), and keyword arguments (specified by name). Understanding these options gives you precise control over how functions receive data.

## Key Concepts

### Positional Parameters and Arguments

Positional parameters are defined in the function signature and must be provided in order when calling the function. The first argument maps to the first parameter, the second to the second, and so on. The order matters, and you must provide the correct number of arguments.

### Default Parameters

Default parameters have preset values in the function definition using the equals sign. If no argument is provided for that parameter when calling the function, the default value is used. Default parameters must come after non-default parameters in the function signature.

### Keyword Arguments

When calling a function, you can specify arguments by parameter name using the syntax `parameter=value`. This allows you to provide arguments in any order and makes code more readable by explicitly showing which value goes to which parameter. Keyword arguments are particularly useful with multiple parameters or when using defaults.

## Example

```python
# Positional parameters
def introduce(first_name, last_name, age):
    print(f"My name is {first_name} {last_name} and I'm {age} years old")

introduce("John", "Smith", 30)  # Order matters

# Default parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Uses default greeting
greet("Bob", "Hi")  # Overrides default

# Keyword arguments
def create_profile(username, email, age=18, active=True):
    print(f"User: {username}, Email: {email}, Age: {age}, Active: {active}")

# Mix of positional and keyword
create_profile("jsmith", "j@example.com", age=25)

# All keyword arguments (order doesn't matter)
create_profile(active=False, email="b@example.com", username="bjones", age=30)
```

## Your Task

You'll practice defining functions with parameters and calling them with various argument types: positional arguments, default parameters, and keyword arguments.
