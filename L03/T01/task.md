Logical operators combine or modify boolean values (`True`/`False`). They're essential for making complex decisions in your code.

## The Three Logical Operators

**`and`** – Returns `True` only if both conditions are true

```python
has_ticket = True
has_id = True
can_enter = has_ticket and has_id  # True
```

**`or`** – Returns `True` if at least one condition is true

```python
is_student = False
is_senior = True
gets_discount = is_student or is_senior  # True
```

**`not`** – Inverts the boolean value

```python
is_raining = False
go_outside = not is_raining  # True
```

## Combining Operators

You can combine operators for complex conditions:

```python
is_adult = True
has_permission = False
can_proceed = is_adult and not has_permission  # False
```
