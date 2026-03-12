# String Indexes

## Indexing a string

Strings are ordered sequences of characters.
Indexing starts at 0.

```python
text = "Data Science"
text[0]   # 'D'
text[-1]  # 'e' (negative indexes count from the end)
```

## Slicing a string

Slicing uses `[start:stop:step]` and returns a new string.
`start` is inclusive, `stop` is exclusive.

```python
text[1:4]   # 'ata'
text[5:]    # from index 5 to the end
text[:]     # full copy of the string
text[2:9]   # stop beyond length is allowed too
```

## Negative indexes in slices

Negative values count from the end:

```python
text[:-4]  # everything except the last 4 characters
text[-4:]  # last 4 characters
```

## Step and reverse

The step controls how many characters to skip.
A step of `-1` reverses the string.

```python
text[::2]   # every second character
text[::-1]  # reversed string
```
