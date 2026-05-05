A generator is a special kind of function that produces values one by one instead of returning them all at once. This is useful when working with long sequences, because generators do not store all values in memory at the same time.

A generator uses the yield keyword instead of return. When Python reaches yield, it sends a value and pauses the function. The next time the generator is used, execution continues from that exact place.

Because of this behavior, generators are memory-efficient and convenient for sequences that can be built step by step.

```python
def count_up_to(number):
    for x in range(number):
        yield x
```

This function does not create the whole list immediately. Instead, it generates one value at a time.

To see all generated values at once, you can convert the generator to a list:

```python
result = list(count_up_to(5))
```

This produces:

```
[0, 1, 2, 3, 4]
```

Generators are especially useful for mathematical sequences, including the Fibonacci sequence.

### Fibonacci numbers

The Fibonacci numbers form a sequence in which each number is the sum of the two previous ones. It usually starts with 0 and 1, so the sequence begins like this:

```
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Here is how they are calculated:

- **first number:** 0
- **second number:** 1
- **each next number:** sum of the previous two numbers

For example:

```
1 = 0 + 1
2 = 1 + 1
3 = 1 + 2
5 = 2 + 3
```

In this task, you need to write a generator that yields Fibonacci numbers one by one.