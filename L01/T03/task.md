# String Formatting

Python provides multiple ways to insert values into strings.

**Using .format() method:**

```python
name = "Alice"
age = 25
print("Hello {}, you are {} years old.".format(name, age))
# Output: Hello Alice, you are 25 years old.
```

You can use positional indexes:

```python
print("{0} is {1} years old. {0} lives in Paris.".format("Bob", 30))
# Output: Bob is 30 years old. Bob lives in Paris.
```

Or named placeholders:

```python
print("{name} earned {score} points.".format(name="Carol", score=95))
# Output: Carol earned 95 points.
```

**Using f-strings (Python 3.6+):**

F-strings provide a simpler syntax by placing variable names directly in the string:

```python
city = "Tokyo"
population = 14
print(f"{city} has {population} million people.")
# Output: Tokyo has 14 million people.
```

## Your Task

Complete the string formatting exercises using the appropriate method specified in each comment.
