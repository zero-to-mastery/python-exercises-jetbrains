# Augmented Assignment Operators

Augmented assignment operators provide a shorthand for updating variables. Instead of writing `counter = counter + 1`, you can write `counter += 1`.

**Common operators:**

```python
x = 10
x += 5   # x = x + 5   → x is now 15
x -= 3   # x = x - 3   → x is now 12
x *= 2   # x = x * 2   → x is now 24
x //= 4  # x = x // 4  → x is now 6
```

Each operator performs the arithmetic operation and updates the variable in one step. The operations build on the previous value.

**Example - tracking inventory:**

```python
inventory = 100
inventory += 50   # received shipment, now 150
inventory -= 30   # sold items, now 120
```

## Your Task

Complete the code using augmented assignment operators to achieve the target values specified in the comments.
