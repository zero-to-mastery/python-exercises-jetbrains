# Tuples

## What Are Tuples?

Tuples are **immutable sequences** - ordered collections that cannot be changed after creation. They use parentheses `()` instead of square brackets.

```python
my_tuple = (1, 2, 3)
coordinates = (10.5, 20.3)
```

## Key Characteristics

### Immutability
Once created, tuples cannot be modified - no adding, removing, or changing elements. This makes them:
- Faster than lists
- Safe for storing constant data
- Usable as dictionary keys

### Syntax
Like lists, tuples use comma-separated values:
```python
regular = (1, 2, 3)
single = (5,)  # Note: comma required for single-element tuples!
```

**Important:** Without the trailing comma, `(5)` is just a number in parentheses, not a tuple.

## Operations Like Lists

Tuples support read-only operations:
- **Indexing**: `my_tuple[0]` accesses first element
- **Length**: `len(my_tuple)` returns number of elements
- **Unpacking**: `x, y, z = my_tuple` assigns values to variables
- **Iteration**: Can loop through elements

## When to Use Tuples

Use tuples when:
- Data shouldn't change (coordinates, RGB colors, database records)
- You need better performance
- You want to use the data as dictionary keys
- You want to prevent accidental modifications

Use lists when data needs to be modified.
