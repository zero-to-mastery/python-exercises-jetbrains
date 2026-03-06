# Matrix Operations

## What You'll Learn

Access elements in nested lists (lists within lists) using multiple index operations to navigate hierarchical data structures.

## Concept Overview

Nested lists, also called multi-dimensional lists, are lists that contain other lists as elements. This structure is useful for representing tabular data, grids, matrices, or any hierarchical information like organizational charts or nested categories. Accessing elements deep within nested structures requires chaining multiple index operations together.

## Key Concepts

### Nested List Structure

A nested list is created when lists are placed inside other lists:

```python
simple_nested = [[1, 2], [3, 4]]
deeply_nested = [["a", ["b", "c"]], ["d"]]
```

### Accessing Elements

Each level of nesting requires one index operation:

```python
data = [["red", "blue"], ["green", "yellow"]]
outer = data[0]           # ["red", "blue"]
inner = data[0][1]        # "blue"
```

### Multi-Level Access

For deeply nested structures, chain indices from outer to inner:

```python
tree = [[["leaf1", "leaf2"], ["leaf3"]], [["leaf4"]]]
value = tree[0][1][0]     # Accesses "leaf3"
```

Each index navigates one level deeper: first index selects from the outermost list, second index from the next level, and so on.

## Example

```python
# A shopping cart with categories
cart = [
    ["Electronics", ["Laptop", "Mouse"]],
    ["Books", ["Python Guide", "Web Dev"]]
]

# Access the first book
first_book = cart[1][1][0]  # Returns "Python Guide"

# Breaking it down:
# cart[1] gets ["Books", ["Python Guide", "Web Dev"]]
# cart[1][1] gets ["Python Guide", "Web Dev"]
# cart[1][1][0] gets "Python Guide"
```

## Your Task

Practice navigating through nested list structures using index notation. The code contains a nested list where you need to access a specific element buried several levels deep. Focus on understanding how each index operation moves one level deeper into the structure.
