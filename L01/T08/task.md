# Nested List Access

Lists in Python can contain other lists as elements, creating multi-dimensional or nested structures. Accessing elements in nested lists requires understanding how indexing works at each level.

## How Nested List Indexing Works

When you have a nested list like `inventory = [["hammer", "nails"], ["screws", "bolts"]]`:
- `inventory[0]` returns the entire first inner list: `["hammer", "nails"]`
- `inventory[1]` returns the entire second inner list: `["screws", "bolts"]`
- `inventory[0][1]` first accesses `inventory[0]` (which is `["hammer", "nails"]`), then accesses index `[1]` of that list (which is `"nails"`)

## Task

Practice accessing elements from nested lists by navigating through multiple levels of indices. Remember to work from left to right, one level at a time.
