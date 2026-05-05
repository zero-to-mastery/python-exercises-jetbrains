A **lambda function** is a compact way to define a simple function without `def`. It consists of parameters and one expression whose value is returned automatically. Lambda functions are often used when the logic is short and needed only once.

The **`map()`** function applies a function to each element of an iterable and returns an iterator. To get the final values in a regular list, the result is usually wrapped in `list()`. This is a common way to transform all elements of a collection in the same way.

The **`sort()`** method changes the original list and arranges its elements in order. When the elements are complex objects such as tuples, the `key` argument tells Python which part of each element should be used for comparison. Tuple elements are accessed by index: `0` for the first item, `1` for the second.

```python
numbers = [1, 2, 3]

# Add 10 to each number and convert the result to a list
result = list(map(lambda x: x + 10, numbers))
```