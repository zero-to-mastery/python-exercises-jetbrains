# Defining and Calling Functions

## What You'll Learn

How to define reusable functions with the def keyword and call them to execute their code multiple times.

## Concept Overview

Functions are reusable blocks of code that perform specific tasks. By defining a function once, you can call it many times throughout your program, promoting code reuse and organization. Functions help break down complex problems into manageable pieces and make code more maintainable.

The `def` keyword creates a function definition, followed by the function name, parentheses, and a colon. The indented code block that follows is the function body, which executes each time the function is called.

## Key Concepts

### Function Definition

A function definition starts with `def`, followed by a name that describes what the function does. The name should use lowercase with underscores between words. After the name come parentheses (empty if no parameters) and a colon. The function body is indented and contains the code to execute.

### Calling Functions

To execute a function, use its name followed by parentheses. This is called "calling" or "invoking" the function. Each call executes the function body once. Functions can be called multiple times, and each call is independent.

### Code Reusability

Functions eliminate code duplication. Instead of writing the same code multiple times, you write it once in a function and call that function whenever needed. This makes programs shorter, easier to maintain, and less prone to errors from inconsistent duplicated code.

## Example

```python
# Define a function
def greet():
    print("Welcome!")
    print("How can I help you today?")

# Call the function multiple times
greet()  # First call
print()
greet()  # Second call

# A more complex example
def print_separator():
    print("=" * 40)

print_separator()
print("Important Information")
print_separator()
print("This section contains key details")
print_separator()

# Function with loop
def show_menu():
    options = ["View Profile", "Settings", "Logout"]
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

show_menu()
```

## Your Task

You'll practice defining functions using def and calling them multiple times to execute their code, demonstrating how functions enable code reuse.
