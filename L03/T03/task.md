# Nested Loops

## What Are Nested Loops?

A nested loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

## How Nested Loops Work

When working with 2D data (like a grid or matrix), you typically use two loops:

**Outer loop** – iterates through rows

```python
for row in grid:
    # processes each row
```

**Inner loop** – iterates through elements in each row

```python
for row in grid:
    for item in row:
        print(item)
```

## Controlling Output Format

Use `print()` parameters to control how output appears:

* `end=""` – prevents moving to a new line after printing
* `print('')` – moves to a new line

```python
print('A', end="")  # prints 'A' without newline
print('B', end="")  # prints 'B' on the same line
print('')           # moves to next line
```

In this task, use nested loops to display ASCII art from the 2D list picture: `0` should become a space, `1` should become `*`, and each row should be printed on a **separate line**.

Please note that you should print `|` at the beginning and end of each row.

```python
|   *   |
|  ***  |
| ***** |
|*******|
|   *   |
|   *   |
```

<div class="hint">
You'll need an outer loop for rows and an inner loop for pixels. Use a conditional to decide which character to print.
</div>
