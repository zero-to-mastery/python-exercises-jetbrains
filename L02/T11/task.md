# Matrix Operations

## What Are Nested Lists?

Lists can contain other lists as elements. These "lists within lists" are called **nested lists** or **multi-dimensional lists**. They're useful for representing complex data structures like grids, tables, or hierarchical data.

```python
simple_list = [1, 2, 3]
nested_list = [1, [2, 3], 4]
deeply_nested = ["a", ["b", ["c", "d"], "e"], "f"]
```

## Accessing Nested Elements

To access elements in nested lists, use **chained indexing** - apply multiple index operations one after another:

```python
data = ["first", ["second", "third"], "fourth"]

# Access the nested list at index 1
data[1]  # Returns ["second", "third"]

# Chain indices to access elements within the nested list
data[1][0]  # Returns "second"
data[1][1]  # Returns "third"
```

## How It Works

Each index operation selects one level deeper:
- First index: selects from the outer list
- Second index: selects from the list you just accessed
- Third index: goes even deeper (if nested further)

Think of it like drilling down through layers - each index takes you one layer deeper into the structure.

