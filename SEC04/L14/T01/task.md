# Encapsulation

## What You'll Learn

Understand encapsulation, one of the core principles of OOP, which bundles data and methods together while controlling access to internal state.

## Concept Overview

Encapsulation is the practice of bundling data (attributes) and the methods that operate on that data within a single unit (class), while restricting direct access to some components. This protects the internal state of objects from unintended interference and misuse.

Encapsulation promotes modularity, makes code easier to maintain, and allows you to change internal implementation without affecting code that uses your class.

## Key Concepts

### Bundling Data and Behavior

Classes combine related data and functions:

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # Controlled access
```

### Controlled Access

Provide methods to interact with data rather than direct access:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32
```

### Information Hiding

Hide internal implementation details from external code:

```python
class Engine:
    def start(self):
        self._inject_fuel()  # Internal method
        self._ignite()       # Internal method
        return "Engine started"
```

## Example

```python
class Thermostat:
    def __init__(self, temperature):
        self._temperature = temperature
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        return "Thermostat is on"

    def set_temperature(self, temp):
        if 60 <= temp <= 80:  # Validation
            self._temperature = temp
            return f"Temperature set to {temp}"
        return "Invalid temperature"

    def get_status(self):
        status = "on" if self._is_on else "off"
        return f"Thermostat is {status} at {self._temperature}°F"

thermo = Thermostat(70)
thermo.turn_on()
print(thermo.set_temperature(75))
print(thermo.get_status())
```

## Your Task

Explore how encapsulation bundles data with the methods that operate on it. Understand how providing methods for data access creates a controlled interface to your objects.
