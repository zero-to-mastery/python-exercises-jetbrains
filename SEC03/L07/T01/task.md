# Conditional Logic with if, elif, and else

## What You'll Learn

How to control program flow using conditional statements and logical operators to make decisions based on multiple conditions.

## Concept Overview

Conditional logic allows programs to make decisions and execute different code based on whether conditions are true or false. Python uses `if`, `elif` (else if), and `else` statements to create branching logic paths. These statements evaluate Boolean expressions and execute code blocks accordingly.

Logical operators like `and`, `or`, and `not` allow you to combine multiple conditions into more complex expressions. This enables sophisticated decision-making where multiple factors determine which code path to execute.

## Key Concepts

### The if-elif-else Chain

An `if` statement checks a condition and executes its code block if true. The `elif` statement provides alternative conditions to check if previous conditions were false. The `else` statement provides a default action when all other conditions fail. Only the first true condition's block executes, even if multiple conditions are true.

### Logical Operators

The `and` operator returns True only if both conditions are true. The `or` operator returns True if at least one condition is true. The `not` operator inverts a Boolean value. These operators allow you to express complex business logic clearly and concisely.

### Short-Circuit Evaluation

Python evaluates conditions from left to right and stops as soon as the result is determined. For `and`, if the first condition is false, the second is never checked. For `or`, if the first condition is true, the second is never checked. This behavior can affect performance and side effects in your conditions.

## Example

```python
temperature = 75
is_sunny = True

if temperature > 80 and is_sunny:
    print("It's hot and sunny - go to the beach!")
elif temperature > 80:
    print("It's hot but not sunny - maybe stay indoors")
elif is_sunny:
    print("It's sunny but cool - perfect for a walk")
else:
    print("It's cool and cloudy - good reading weather")

# Using logical operators
has_umbrella = False
is_raining = True

if is_raining and not has_umbrella:
    print("You'll get wet!")
elif is_raining and has_umbrella:
    print("You're prepared!")
```

## Your Task

You'll practice writing conditional statements using if, elif, and else, and combining multiple conditions using the and, or, and not logical operators to create decision-making logic.
