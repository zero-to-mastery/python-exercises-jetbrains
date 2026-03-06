# Under the Hood Generators

## What You'll Learn

Understand how generators work internally using the iterator protocol, and explore advanced generator features.

## Concept Overview

Generators are built on Python's iterator protocol. Each call to next() executes the generator until it hits a yield, then pauses.

## Key Concepts

### Iterator Protocol

```python
def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
```

### Generator State

```python
def counter():
    count = 0
    while True:
        count += 1
        yield count
```

### send() Method

```python
def receiver():
    while True:
        value = yield
        print(f"Received: {value}")

gen = receiver()
next(gen)
gen.send("hello")
```

## Example

```python
def running_average():
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        total += value
        count += 1
        average = total / count

avg = running_average()
next(avg)
print(avg.send(10))
print(avg.send(20))
```

## Your Task

Explore how generators work internally and practice using next() and send().
