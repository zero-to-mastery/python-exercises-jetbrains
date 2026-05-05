# Formatted Strings

## Mutable vs Immutable

A mutable object can be changed after it is created.  
Examples: `list`, `dict`, `set`.

An immutable object cannot be changed after it is created.  
Examples: `str`, `int`, `float`, `tuple`.

Strings are immutable, so any “change” to a string actually creates and returns a new string.

## String formatting with format()

`str.format()` inserts values into a string.
It returns a new string (strings are immutable).

```python
"Hello {}, you have {} messages.".format("Alex", 3)
```

### Positional placeholders

Use `{0}`, `{1}`, ... to refer to arguments by index:

```python
"Hello {0}, you have {1} messages.".format("Alex", 3)
```

### Named placeholders

Use names inside braces and pass keyword arguments:

```python
"Hello {name}, you have {count} messages.".format(name="Alex", count=3)
```

## f-strings

Prefix a string with `f` and put expressions inside `{}`.
This is often the most readable option.

```python
name = "Alex"
count = 3
f"Hello {name}, you have {count} messages."
```
