Decorators are functions that modify or enhance the behavior of other functions without changing their code. They "wrap" a function to add functionality before or after it runs.

## How Decorators Work

A decorator is a function that:
1. Takes another function as an argument
2. Defines an inner wrapper function that adds new behavior
3. Returns the wrapper function

**Basic syntax:**

```python
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # code before the function
        result = fn(*args, **kwargs)
        # code after the function
        return result
    return wrapper
```

**Using a decorator:**

```python
@my_decorator
def greet(name):
    print(f"Hello {name}")
```

The `@my_decorator` syntax is equivalent to:
```python
greet = my_decorator(greet)
```

## Practical Use: Authentication

Decorators are commonly used to check permissions before allowing a function to execute.

Example pattern:
```python
def check_permission(fn):
    def wrapper(*args, **kwargs):
        if user_has_permission:
            return fn(*args, **kwargs)
        else:
            print("Access denied")
    return wrapper
```

Your task is to create an `authenticated` decorator that checks if a user is valid before allowing a function to run.

The decorator should:
- Check if the first argument has a `'valid'` key set to `True`
- If valid, execute the function normally
- If not valid, print `"invalid user"` instead
