# Strings in Python

## What Is a String?

A string (`str`) is Python’s text type. Strings store characters (letters, numbers, symbols) in order. You create them using quotes:

```python
text = 'Hello'
```

Strings are immutable, which means methods don’t change the original string — they return a new one.

## Building Strings

You can create new strings using operators.

### Concatenation

Concatenation joins strings with `+`:

```python
full = 'Hello' + ' ' + 'World'
```

### Repetition

Repetition repeats a string with `*`:

```python
triple = 'Python' * 3
```

If you want to join text with a number, convert the number to a string first using `str()`:

```python
message = 'hello ' + str(5)
```

## Useful String Tools

### Case and Cleanup

- `upper()` makes all letters uppercase
- `lower()` makes all letters lowercase
- `strip()` removes whitespace from the left and right sides

### Search and Replace

- `find(sub)` returns the index of the first match (or `-1` if not found)
- `replace(old, new)` returns a new string where `old` is replaced by `new`

### Length

- `len(text)` returns the number of characters in a string
