# Type Conversion

Python allows you to convert between different data types using built-in functions.

**Common conversion functions:**

```python
int("123")      # '123' → 123 (string to integer)
float("3.14")   # '3.14' → 3.14 (string to float)
str(42)         # 42 → '42' (integer to string)
```

**Why convert types?**

String values cannot be used in arithmetic operations. You must convert them first:

```python
age_str = "25"
next_year = int(age_str) + 1    # Convert, then add
```

**Converting to strings:**

Numbers must be converted to strings for concatenation:

```python
score = 100
message = "Score: " + str(score)    # 'Score: 100'
```

## Your Task

Practice converting between strings, integers, and floats to perform calculations and create formatted output.
