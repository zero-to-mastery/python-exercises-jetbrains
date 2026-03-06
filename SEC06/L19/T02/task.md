# Guessing Game Testing Project

## What You'll Learn

Apply unit testing principles to a complete project by writing comprehensive tests for a guessing game application.

## Concept Overview

This exercise builds on basic testing concepts by applying them to a more complex program. You'll practice writing tests for a guessing game that validates user input, handles errors, and implements game logic.

Testing complete applications requires thinking about all possible inputs, edge cases, and error conditions. Good tests verify not just the happy path (when everything works), but also how the code handles invalid input and boundary conditions.

## Key Concepts

### Testing Game Logic

Test the core functionality:

```python
def test_correct_guess(self):
    result = run_guess(5, 5)
    self.assertTrue(result)

def test_wrong_guess(self):
    result = run_guess(3, 5)
    self.assertFalse(result)
```

### Testing Input Validation

Verify that the game handles invalid input:

```python
def test_out_of_range(self):
    result = run_guess(15, 5)
    self.assertFalse(result)

def test_invalid_type(self):
    with self.assertRaises(ValueError):
        run_guess('abc', 5)
```

### Testing Edge Cases

Consider boundary conditions:

```python
def test_minimum_value(self):
    result = run_guess(1, 1)
    self.assertTrue(result)

def test_maximum_value(self):
    result = run_guess(10, 10)
    self.assertTrue(result)
```

### Comprehensive Test Coverage

A complete test suite covers:
- Correct behavior (happy path)
- Invalid input handling
- Edge cases and boundaries
- Error conditions

## Example

```python
import unittest
from game import check_guess

class TestGuessingGame(unittest.TestCase):
    def test_exact_match(self):
        self.assertTrue(check_guess(7, 7))
    
    def test_too_low(self):
        self.assertFalse(check_guess(3, 7))
    
    def test_too_high(self):
        self.assertFalse(check_guess(9, 7))
    
    def test_boundary_low(self):
        self.assertTrue(check_guess(1, 1))
    
    def test_boundary_high(self):
        self.assertTrue(check_guess(10, 10))
    
    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            check_guess('five', 7)

if __name__ == '__main__':
    unittest.main()
```

## Your Task

Study how to write comprehensive tests for a complete application. Practice testing different scenarios: correct guesses, wrong guesses, boundary values, and invalid input. Learn to use assertRaises for exception testing and understand how thorough testing improves code reliability.
