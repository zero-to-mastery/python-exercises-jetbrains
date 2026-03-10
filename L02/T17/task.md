# Tuples

## Theory

A tuple is an ordered collection of items, similar to a list, but **immutable** (you cannot change its elements after it is created). Tuples are written with parentheses: `(1, 2, 3)`. They are often used to store data that should not be modified, or to group a few values together (for example: coordinates `(x, y)` or an RGB color `(255, 0, 0)`).

## Accessing Items

You can access tuple items by index, just like with lists: `t[0]` is the first element. You can also check if a value is inside a tuple using `in`.

## Unpacking

Tuples support **unpacking**, which means assigning tuple elements to multiple variables in one line. With the `*` operator, you can collect the rest of the elements into a list, for example:

```python
a, b, *rest = (1, 2, 3, 4)
```

## Useful Methods

Two useful tuple methods are:

- `count(value)` returns how many times `value` appears in the tuple.
- `index(value)` returns the index of the first occurrence of `value` (and raises an error if the value is not found).
