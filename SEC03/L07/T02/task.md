# Logical Operators Exercise

## What You'll Learn

How to combine boolean conditions using and, or, and not operators to create complex conditional logic.

## Concept Overview

Logical operators allow you to combine multiple Boolean expressions into a single condition. This is essential for expressing real-world logic where decisions depend on multiple factors. The three primary logical operators in Python are `and`, `or`, and `not`.

These operators enable you to write precise conditional statements that check multiple criteria simultaneously, making your code more expressive and closer to natural language reasoning.

## Key Concepts

### The AND Operator

The `and` operator returns True only when all conditions it connects are True. If any condition is False, the entire expression evaluates to False. This is used when all requirements must be met for an action to occur.

### The NOT Operator

The `not` operator inverts a Boolean value, turning True into False and False into True. This is useful for checking the opposite of a condition, such as when something should NOT be true for an action to proceed.

### Combining Multiple Operators

You can combine and, or, and not operators to create complex logical expressions. Understanding operator precedence is important: `not` has the highest precedence, followed by `and`, then `or`. Use parentheses to make your intentions clear and override default precedence.

## Example

```python
has_ticket = True
has_id = False
is_adult = True

# Using AND - all conditions must be true
if has_ticket and has_id and is_adult:
    print("Welcome to the concert!")

# Using AND with NOT - checking negative conditions
if has_ticket and not has_id:
    print("You need to show ID")

# Using NOT alone - checking if something is false
if not has_ticket:
    print("Please purchase a ticket")

# Complex combination
is_student = True
if has_ticket and is_adult and (not has_id or is_student):
    print("Conditional entry granted")
```

## Your Task

You'll practice using logical operators to create conditional statements that check multiple boolean values, including using and to require multiple conditions, not to invert conditions, and combining operators for more sophisticated logic.
