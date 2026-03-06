# Ternary Operator

## What You'll Learn

How to write concise conditional expressions using Python's ternary operator for simple if-else assignments.

## Concept Overview

The ternary operator provides a compact way to write simple if-else statements in a single line. It evaluates a condition and returns one value if true, another if false. The syntax is: `value_if_true if condition else value_if_false`.

This operator is particularly useful for conditional assignments where you want to set a variable to one value or another based on a condition. It makes code more readable when the logic is straightforward, though complex conditions should still use traditional if-else statements.

## Key Concepts

### Ternary Syntax

The ternary operator has three parts: the value to return if true, the condition to test, and the value to return if false. Reading from left to right: "give me this value IF this condition is true ELSE give me that value." This order differs from traditional if-else statements.

### Use Cases

Ternary operators excel at simple conditional assignments, setting default values, or choosing between two options based on a single condition. They reduce code verbosity for straightforward decisions. However, they can become hard to read if the condition or values are complex.

### Return Values

The ternary operator is an expression, meaning it returns a value. This is different from an if-else statement, which is a control flow structure. You can assign the result of a ternary expression directly to a variable, use it in function arguments, or embed it in other expressions.

## Example

```python
# Simple conditional assignment
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Using with function calls
score = 85
result = "Pass" if score >= 60 else "Fail"
print(result)  # Pass

# In print statements
is_weekend = True
print("Sleep in!" if is_weekend else "Set alarm")

# Chaining (not recommended, reduces readability)
grade = 95
letter = "A" if grade >= 90 else "B" if grade >= 80 else "C"

# Traditional if-else for comparison
temperature = 30
if temperature > 25:
    clothing = "shorts"
else:
    clothing = "pants"

# Equivalent ternary
clothing = "shorts" if temperature > 25 else "pants"
```

## Your Task

You'll practice using the ternary operator to write concise conditional expressions that assign different values based on boolean conditions.
