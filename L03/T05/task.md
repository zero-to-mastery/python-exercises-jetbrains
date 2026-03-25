A function can accept information from outside. This information is passed into the function through **parameters**.

A **parameter** is a variable written inside the parentheses in the function definition:

```python
def greet(name):
    print("Hello,", name)
```
Here, `name` is a parameter.

When you call the function, you pass an argument — the actual value the function should use:
```python
greet("Alice")
```
In this call, "Alice" is the argument.

Using parameters makes functions more flexible, because the same function can work with different values.

You can also give a parameter a **default value**:
```python
def greet(name="Guest"):
    print("Hello,", name)
```
If no argument is passed, the default value is used.


In this task, the function should accept an `age` parameter instead of using `input()`. It should also use a default value, so the function can still work even if no argument is given.

<div class='hint'>Make sure the function has an <code>age</code> parameter and that its default value is <code>0</code>.</div>