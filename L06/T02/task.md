## Refactoring code for testing

We already have a working version of the game in `initial_solution.py`, but it is written **inline**: the whole program starts running as soon as the file is executed or imported. This makes the code harder to test, because the game loop, input handling, random number generation, and guess-checking logic are all mixed together.

Your task now is to **refactor** that solution into a more testable format so that it passes the tests in `test.py`.

### Why refactor?

When logic is written inline, tests cannot easily call just the part they need. For example, if a file immediately starts asking for input, a test cannot simply check whether one guess is correct or not.

A better structure is:

* put the core logic into a function;
* keep interactive code inside `if __name__ == '__main__':`.

This way, the function can be imported and tested separately, while the full game still works when the file is run normally.

For example, compare these two ideas:

```python
# hard to test
price = int(input())
if price < 0:
    print("Invalid")
```

```python
# easy to test
def check_price(price):
    return price >= 0

if __name__ == '__main__':
    price = int(input())
    print(check_price(price))
```

In the second version, `check_price()` can be tested directly with many inputs.

### What the tests expect

The tests import your file as a module:

```python
import main
```

and then call:

```python
main.run_guess(5, 5)
```

So your solution must define a function named `run_guess` that takes:

1. `guess`
2. `answer`

and returns `True` or `False`.

In this task, the tests use boolean assertions such as `assertTrue()` and `assertFalse()`, so the return value matters.

### What your function should do

Your `run_guess()` function should return:

* `True` if the guess is correct;
* `False` if the guess is incorrect;
* `False` if the input is invalid, for example:

  * the number is out of range;
  * the value has the wrong type.

Now open `test.py`, look at what cases are checked there, and refactor the original inline solution so that all tests pass.
