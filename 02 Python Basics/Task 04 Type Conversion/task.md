# Type Conversion

## The Problem

Look at the code in `5-ExerciseTypeConversion.py`. You'll see:
```python
birth_year = '1990'  # This is a string!
age = 2026 - birth_year
```

If you run this code, you'll get an error. Why?

## Understanding Types

Python has different data types:
- **Strings** - text in quotes: `'1990'`, `"hello"`
- **Integers** - whole numbers: `1990`, `42`, `-5`
- **Floats** - decimals: `3.14`, `2.5`

Each type has different capabilities. You can't perform math directly on strings!

## Type Conversion Functions

Python provides functions to convert between types:

| Function | Purpose | Example Input | Example Output |
|----------|---------|---------------|----------------|
| `int()` | Convert to integer | `'1990'` | `1990` |
| `float()` | Convert to float | `'3.14'` | `3.14` |
| `str()` | Convert to string | `1990` | `'1990'` |

## How to Use Conversion Functions

Wrap the value you want to convert:
```python
text_number = '42'
real_number = conversion_function(text_number)
```

## Your Task
The variable `birth_year` is currently a string. To use it in math, you need to convert it to a number type first.
