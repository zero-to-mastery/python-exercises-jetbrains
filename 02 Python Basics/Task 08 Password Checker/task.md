# Password Checker

## What Is Password Masking?

When applications display passwords, they often hide the actual characters by replacing them with asterisks (`*`). This protects privacy by preventing others from seeing the password on screen.

For example:
- Actual password: `super_secret`
- Displayed password: `************`

## String Operations Needed

### String Repetition
You can repeat strings using the `*` operator:
```python
character * number  # Repeats the character 'number' times
```

### String Length
The `len()` function returns how many characters are in a string:
```python
len('hello')  # Returns 5
```
