# List Methods

## What Are List Methods?

Methods are built-in functions that belong to specific data types. Lists come with powerful methods that let you add, remove, find, and manipulate elements. These methods modify the list directly rather than creating a new one.

## Common List Methods

### Adding Elements
- **append()** - Adds an item to the end of the list
- **insert()** - Adds an item at a specific position
- **extend()** - Adds all items from another list to the end

### Removing Elements
- **remove()** - Removes the first occurrence of a specific value
- **pop()** - Removes and returns an item at a specific position (or the last item if no position given)
- **clear()** - Removes all items from the list

### Finding Information
- **count()** - Returns how many times a value appears in the list
- **index()** - Returns the position of the first occurrence of a value

### Reordering and Copying
- **sort()** - Sorts the list in place
- **reverse()** - Reverses the list in place
- **copy()** - Creates a shallow copy of the list

## Method Syntax

Methods are called using dot notation:

```python
my_list.method_name(arguments)
```

Some methods need arguments (values to work with), others don't:
- `basket.append("Kiwi")` - needs the item to add
- `basket.remove("Banana")` - needs the item to remove
- `basket.count("Apples")` - needs the item to count

## Mutability Reminder

List methods typically **modify the original list** - they don't create a copy. After calling a method, your list has changed.
Most list methods return `None` because the list itself is modified.


