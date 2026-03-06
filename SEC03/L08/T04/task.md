# While Loops

## What You'll Learn

How to use while loops to repeat code based on a condition, including loop control with break statements and else clauses.

## Concept Overview

While loops repeat a block of code as long as a condition remains true. Unlike for loops that iterate over a known sequence, while loops continue indefinitely until their condition becomes false. This makes them ideal for situations where you don't know in advance how many iterations are needed.

While loops require careful management to avoid infinite loops. You typically need to modify a variable within the loop body that eventually makes the condition false, or use a break statement to exit the loop explicitly.

## Key Concepts

### Condition-Based Looping

A while loop checks its condition before each iteration. If the condition is true, the loop body executes; if false, the loop ends. The condition can be any Boolean expression. It's crucial to ensure the condition can eventually become false, or you'll create an infinite loop.

### Loop Else Clause

Python's while loops can have an optional else clause that executes when the loop completes normally (condition becomes false) but not when the loop is exited with break. This is useful for distinguishing between normal completion and early termination.

### Break for Early Exit

The break statement immediately exits the loop, regardless of the condition. This is commonly used with infinite loops (while True) where you check for a specific condition inside the loop body to decide when to exit. This pattern is useful for input validation or event-driven loops.

## Example

```python
# Basic counter loop
count = 0
while count < 5:
    print(count)
    count += 1  # Must modify to avoid infinite loop

# Using else clause
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop completed naturally")

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")

# While loop with list
items = ['a', 'b', 'c']
index = 0
while index < len(items):
    print(items[index])
    index += 1
```

## Your Task

You'll practice writing while loops with conditions, using else clauses, implementing infinite loops with break statements for controlled exit, and iterating through collections with while loops.
