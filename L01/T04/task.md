# String Slicing

String slicing lets you extract parts of a string using bracket notation with start and stop positions.

**Basic syntax:**

```python
text = "Python"
text[1:4]    # 'yth' - characters from index 1 to 3 (stop-1)
text[2:]     # 'thon' - from index 2 to end
text[:3]     # 'Pyt' - from start to index 2
```

**Negative indices:**

Negative numbers count from the end of the string:

```python
text = "Hello"
text[-1]     # 'o' - last character
text[-3:]    # 'llo' - last 3 characters
text[:-2]    # 'Hel' - everything except last 2
```

**Step parameter:**

Add a third value to control the step:

```python
text = "abcdef"
text[::2]    # 'ace' - every 2nd character
text[::-1]   # 'fedcba' - reverse the string
```

## Your Task

Create slices of the given string to extract specific parts. Each slice should produce the result shown in the comments.
