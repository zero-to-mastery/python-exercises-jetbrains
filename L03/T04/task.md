Duplicates are items that appear more than once in a list. Finding duplicates is a common task in data processing.

## Checking for Duplicates

The `.count()` method returns how many times a value appears in a list:

```python
fruits = ['apple', 'banana', 'apple']
fruits.count('apple')  # returns 2
```

You can use this in a condition to identify duplicates:

```python
if my_list.count(value) > 1:
    # value appears more than once
```

## Avoiding Duplicate Results

When collecting duplicates, you need to ensure each duplicate is only added once to your results.

Use an `in` check before adding:

```python
if item not in results:
    results.append(item)
```

<div class="hint">

Use the `.count()` method to check how many times a value appears in the list.
</div>
