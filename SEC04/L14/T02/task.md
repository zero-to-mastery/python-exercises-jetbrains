# Private vs Public Variables

## What You'll Learn

Distinguish between public and private attributes in Python, and understand naming conventions that signal intended access levels.

## Concept Overview

Python uses naming conventions to indicate whether attributes and methods are intended for external use (public) or internal use (private). While Python doesn't enforce true privacy, prefixing names with underscores signals intent to other developers about how components should be used.

This convention-based approach helps maintain encapsulation and prevents accidental misuse of internal implementation details.

## Key Concepts

### Public Attributes

Regular names indicate public access:

```python
class Car:
    def __init__(self, color):
        self.color = color  # Public - intended for external use
```

### Private Attributes

Single underscore prefix suggests internal use:

```python
class Car:
    def __init__(self):
        self._fuel_level = 100  # "Private" - internal use
```

### Name Mangling

Double underscore prefix triggers name mangling:

```python
class Car:
    def __init__(self):
        self.__secret = "value"  # Stronger privacy signal
```

## Example

```python
class CoffeeMachine:
    def __init__(self):
        self.is_on = False          # Public
        self._water_level = 100     # Private (by convention)
        self.__heating_element = 0  # Name mangled

    def brew(self):
        if self._has_enough_water():  # Private method
            self.__heat()              # Name mangled method
            return "Brewing coffee"
        return "Not enough water"

    def _has_enough_water(self):
        return self._water_level > 10

    def __heat(self):
        self.__heating_element = 100

machine = CoffeeMachine()
print(machine.is_on)           # Public - OK
# machine._water_level          # "Private" - discouraged
# machine.__heating_element     # Name mangled - harder to access
```

## Your Task

Learn Python's naming conventions for public and private attributes. Understand how underscores signal intended usage to other developers.
