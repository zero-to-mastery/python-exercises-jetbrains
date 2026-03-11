# String Length and Repetition

Python provides the `len()` function to count characters in a string and the `*` operator to repeat strings.

**Counting characters:**

```python
text = "hello"
length = len(text)    # 5
```

**Repeating strings:**

```python
star = "*"
mask = star * 5       # '*****'
```

**Combining both:**

You can repeat a string based on another string's length:

```python
password = "secret"
masked = "*" * len(password)    # '******'
```

**Practical uses:**

- Creating password masks
- Generating separators or borders
- Padding text to specific lengths

## Your Task

Practice using `len()` to count characters and `*` to repeat strings for various purposes.
