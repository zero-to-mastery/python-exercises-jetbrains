A list comprehension is a compact way to create a list. It consists of an expression followed by for and, optionally, if. It is useful when you want to build a new list from an existing iterable in a shorter and more readable way.

A set stores only unique values. This makes it useful when you need to remove duplicates from a collection. Since sets are unordered, converting a list to a set and back to a list may change the order of elements.

The `count()` method returns how many times a value appears in a list. This can be used inside a condition when you want to select only elements with a certain property.

For example:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

# Keep only even numbers and remove repeated values
result = list(set([x for x in numbers if x % 2 == 0]))
```

Here, the list comprehension selects only even numbers, and `set()` removes repeated values.

### Previous task

In the previous task, where we searched for duplicated values, the solution looked like this:

```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
```

This code works correctly, but it can be rewritten in a shorter way using the tools above. In this task, you need to replace the loop with a list comprehension and use `set()` to keep only unique values.