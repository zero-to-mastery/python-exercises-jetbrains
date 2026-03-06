# Our First Python Program

## What You'll Learn

Create an interactive Python program that accepts user input and displays personalized output.

## Concept Overview

Python programs can interact with users through the console using built-in functions. Two fundamental functions for interaction are:

- **`input()`**: Reads text from the user
- **`print()`**: Displays text to the user

These functions form the foundation of interactive programs, allowing your code to communicate with users dynamically.

## Key Concepts

### The input() Function

The `input()` function pauses program execution and waits for the user to type something. It accepts a prompt string that's displayed to the user:

```python
user_response = input("Enter something: ")
```

The function returns whatever the user typed as a string.

### The print() Function

The `print()` function displays information to the console. You can print strings, variables, or combine them:

```python
print("Hello, World!")
print("Value:", my_variable)
```

### String Concatenation

You can combine strings using the `+` operator to create personalized messages:

```python
greeting = "Hello " + username
```

## Example

```python
age = input("How old are you? ")
print("You are " + age + " years old!")
```

When this runs:
1. The program asks "How old are you?"
2. The user types their age
3. The program displays a personalized response

## Your Task

Practice using `input()` and `print()` to create an interactive program. You'll learn how to:
- Prompt users for information
- Store user input in variables
- Display personalized messages using string concatenation
