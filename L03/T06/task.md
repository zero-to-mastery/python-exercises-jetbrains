# Highest Even Number

## Working with Filtering and Maximum Values

When processing lists, you often need to filter elements based on conditions and then find specific values like the maximum or minimum.

Python provides the `max()` function to find the largest value in a collection:

```python
numbers = [3, 7, 2, 9]
largest = max(numbers)  # returns 9
```

## Filtering Elements

You can build a new list by checking each element with a condition:

```python
numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
    if num > 3:
        result.append(num)
# result is [4, 5]
```

To check if a number is even, use the modulo operator:

```python
if num % 2 == 0:  # True if num is even
```

<div class="hint">
Use the modulo operator (%) to check if a number is even, and the max() function to find the largest value.
</div>
