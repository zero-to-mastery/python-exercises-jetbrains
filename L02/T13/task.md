# Common List Patterns

## Adding items to a list: extend()

`extend()` adds all elements from another list to the end of the current list.
It modifies the list in place (the original list changes).

```python
letters = ['a', 'b']
extra = ['c', 'd']

letters.extend(extra)
# letters is now ['a', 'b', 'c', 'd']
```

Use `extend()` when you already have a list and want to add multiple items from another list.

## Sorting a list in place: sort()

`sort()` arranges items in the list (alphabetical for strings).
It modifies the list in place.

```python
names = ['B', 'A', 'C']
names.sort()
# names is now ['A', 'B', 'C']
```

You can also sort in reverse order:

```python
names.sort(reverse=True)
# names is now ['C', 'B', 'A']
```

## Creating a new sorted list: sorted()

`sorted()` returns a new sorted list and does not change the original one.

```python
names = ['B', 'A', 'C']
sorted_names = sorted(names)

# names is still ['B', 'A', 'C']
# sorted_names is ['A', 'B', 'C']
```

## Reversing a list with slicing: [::-1]

Slicing with `[::-1]` returns a new list in reverse order.
It does not change the original list.

```python
numbers = [1, 2, 3]
reversed_numbers = numbers[::-1]

# numbers is still [1, 2, 3]
# reversed_numbers is [3, 2, 1]
```

## Creating a sequence of numbers: range()

`range()` creates a sequence of numbers.
It does not create a list by itself, but you can convert it to a list with `list()`.

```python
nums = range(1, 5)       # 1, 2, 3, 4
nums_list = list(nums)   # [1, 2, 3, 4]
```

## Joining list items into a string: join()

`join()` combines list items into a single string with a separator.
It is a string method and expects a list of strings.

```python
words = ['Hi', 'my', 'name', 'is', 'JOJO']
sentence = '! '
result = sentence.join(words)

# result is 'Hi! my! name! is! JOJO'
```

## Which one should you use?

Use `list.sort()` when you want to sort the existing list itself.

Use `sorted(list)` when you want to keep the original list unchanged and get a new sorted version.

In this task, you’ll need to add a new friend to the list and then make sure the final output is alphabetically sorted.
