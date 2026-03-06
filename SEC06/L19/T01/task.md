# Basic Testing

## What You'll Learn

Write unit tests using Python's unittest framework to verify that functions behave correctly under different conditions.

## Concept Overview

Testing is a critical part of software development that helps ensure code works as expected and continues to work when changes are made. Unit tests verify that individual functions or methods produce the correct outputs for given inputs.

Python's built-in `unittest` framework provides tools for writing and running tests. Tests are organized into test cases (classes) that contain test methods. Each test method checks a specific behavior or edge case.

## Key Concepts

### The unittest Framework

Create test classes that inherit from `unittest.TestCase`:

```python
import unittest

class TestMyFunction(unittest.TestCase):
    def test_something(self):
        result = my_function(5)
        self.assertEqual(result, 10)
```

### Assertion Methods

unittest provides various assertion methods:

- `assertTrue(x)` - Check if x is True
- `assertFalse(x)` - Check if x is False
- `assertEqual(a, b)` - Check if a equals b
- `assertRaises(Exception)` - Check if code raises an exception

### Test Organization

Each test method should test one specific behavior:

```python
def test_positive_input(self):
    # Test with positive numbers
    pass

def test_zero_input(self):
    # Test edge case with zero
    pass

def test_invalid_input(self):
    # Test error handling
    pass
```

### Running Tests

Tests run automatically when the script is executed:

```python
if __name__ == '__main__':
    unittest.main()
```

## Example

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)
    
    def test_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```

## Your Task

Examine how unit tests verify function behavior using the unittest framework. Understand how to write test cases, use assertion methods, and test different scenarios including edge cases and error conditions.
