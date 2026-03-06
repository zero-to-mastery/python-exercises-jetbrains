# Guessing Game Module

## What You'll Learn

Build a complete Python program that uses modules, command-line arguments, random number generation, loops, exception handling, and user input to create an interactive guessing game.

## Concept Overview

This exercise combines multiple Python concepts into a practical command-line application. You'll work with the `sys` module to access command-line arguments, the `random` module to generate random numbers, exception handling to validate user input, and control flow to manage the game loop.

Creating complete programs like this demonstrates how Python concepts work together to build functional applications. Understanding how to structure programs, handle user input safely, and manage program flow is essential for real-world Python development.

## Key Concepts

### Command-Line Arguments

The `sys.argv` list contains command-line arguments passed to the script:

```python
import sys

# sys.argv[0] is the script name
# sys.argv[1] is the first argument
# sys.argv[2] is the second argument
min_val = int(sys.argv[1])
max_val = int(sys.argv[2])
```

### Random Number Generation

The `random` module provides functions for generating random values:

```python
from random import randint

# Generate random integer between min and max (inclusive)
random_number = randint(1, 10)
```

### Exception Handling

Use try-except blocks to handle invalid user input gracefully:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")
```

### Game Loop Pattern

Interactive programs often use a loop that continues until a win condition:

```python
while True:
    # Get user input
    # Check win condition
    # If won, break
```

## Example

```python
import sys
from random import randint

# Usage: python script.py 1 100
min_num = int(sys.argv[1])
max_num = int(sys.argv[2])
secret = randint(min_num, max_num)

print(f"Guess a number between {min_num} and {max_num}")

while True:
    try:
        guess = int(input("Your guess: "))
        if guess == secret:
            print("You won!")
            break
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")
    except ValueError:
        print("Please enter a number")
```

## Your Task

Study the guessing game implementation that combines modules, command-line arguments, random numbers, loops, and exception handling. Understand how these concepts work together to create an interactive program that accepts a range via command-line arguments and lets users guess a random number within that range.
