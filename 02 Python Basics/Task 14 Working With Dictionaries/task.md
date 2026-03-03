# Working With Dictionaries

Dictionaries store key–value pairs. You access values by key, not by position (like in lists).

```python
student = {'name': 'Alice', 'age': 20}
```

## Core operations

### Create, access, and nested access

Values can be any type — including lists and other dictionaries — so you can access nested elements step by step.

```python
settings = {
    'theme': 'dark',
    'notifications': True,
    'scores': [10, 20, 30]
}

settings['theme']       # access by key
settings['scores'][1]   # nested access (value is a list)
```

### [] vs get()

`d['key']` raises an error if the key doesn’t exist.

`d.get('key')` is safer: returns `None` (or a default value) if missing.

```python
student['age']              # works if 'age' exists
student.get('age')          # safe access
student.get('grade', 'A')   # default value if key is missing
```

### Add and update

```python
student['email'] = 'alice@example.com'     # add new key
student['age'] = 21                        # update existing key
student.update({'age': 22, 'city': 'Rome'})  # update multiple keys
```

## Useful dictionary tools

Check what’s inside (`keys`, `values`, `items`, `in`).

Important: `'x' in d` checks keys.

```python
student.keys()       # all keys
student.values()     # all values
student.items()      # (key, value) pairs

'age' in student                      # key exists?
'alice@example.com' in student.values()  # value exists?
```

## Copy, clear, and remove

```python
backup = student.copy()   # independent copy
student.clear()           # becomes {}

backup.pop('age')         # remove key and return its value
backup.popitem()          # remove and return last inserted (key, value)
```
