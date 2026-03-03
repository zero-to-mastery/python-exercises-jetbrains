# List Slicing

## What Is Slicing?

Slicing lets you extract portions of a list using a range of indices. It's a powerful way to work with subsets of data without modifying the original list.

## Indexing Recap

Before slicing, remember basic indexing:
- **Positive indices** - Count from the start (0, 1, 2, ...)
- **Negative indices** - Count from the end (-1 is last, -2 is second-to-last, ...)

## Slice Syntax

```python
list[start:end]
```

- **start** - First index to include
- **end** - Stop BEFORE this index (not included!)
- Creates a new list with elements from start up to (but not including) end

## List Independence

When you create new lists (through slicing, concatenation, etc.), they are independent:
- Changes to the original don't affect copies
- Changes to copies don't affect the original

