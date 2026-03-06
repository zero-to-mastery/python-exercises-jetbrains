# Walrus Operator

## What You'll Learn

Use the walrus operator (:=) to assign values within expressions, making code more concise in specific situations.

## Concept Overview

The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression. This is useful when you need both the value and want to use it in a condition or loop, avoiding redundant code.

While the walrus operator can make code more concise, it should be used judiciously. Overuse can reduce readability, so reserve it for cases where it genuinely simplifies the code.

## Key Concepts

### Assignment Within Expressions

Assign and use a value in one statement:

```python
# Without walrus operator
length = len(my_list)
if length > 10:
    print(f"List is long: {length}")

# With walrus operator
if (length := len(my_list)) > 10:
    print(f"List is long: {length}")
```

### Use in While Loops

Common pattern for reading input:

```python
# Without walrus
data = input("Enter data: ")
while data != "quit":
    process(data)
    data = input("Enter data: ")

# With walrus
while (data := input("Enter data: ")) != "quit":
    process(data)
```

### Use in List Comprehensions

Filter and transform in one step:

```python
# Calculate expensive operation once
results = [output for item in items 
           if (output := expensive_function(item)) > threshold]
```

### When to Use

Good use cases:
- Avoiding duplicate function calls
- Reducing variable scope
- Simplifying while loop conditions

Avoid when it reduces readability or isn't necessary.

## Example

```python
# Example 1: String length check
text = "Hello, World!"
if (n := len(text)) > 10:
    print(f"Long text with {n} characters")

# Example 2: While loop with input
while (command := input("Command: ")) != "exit":
    print(f"Executing: {command}")
    execute_command(command)

# Example 3: Reducing string in loop
message = "Python Programming"
while (n := len(message)) > 5:
    print(f"Length: {n}")
    message = message[:-1]
```

## Your Task

Explore the walrus operator and understand when it makes code more concise without sacrificing readability. Practice using it in conditionals and loops where you need both assignment and the value in one expression.
