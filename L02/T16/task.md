# Dictionary Methods II

## Theory

In this lesson you’ll use several dictionary methods for copying, removing, updating, and clearing data.

### Copying

`dict.copy()` returns a new dictionary with the same key–value pairs. It’s a *shallow* copy: nested mutable values (like lists) are not copied deeply, so both dictionaries can still refer to the same inner objects.

### Removing entries

`dict.pop(key)` removes the given key from the dictionary and returns its value. If the key doesn’t exist, it raises `KeyError` unless you provide a default value: `pop(key, default)`.

`dict.popitem()` removes and returns a `(key, value)` pair. In modern Python it removes the last inserted item (useful for “take the last added entry”).

### Updating

`dict.update(other)` adds or overwrites keys from another dictionary (or any iterable of key–value pairs). Existing keys get replaced with the new values, and new keys are added.

### Clearing

`dict.clear()` removes all items from the dictionary, leaving it empty (`{}`).
