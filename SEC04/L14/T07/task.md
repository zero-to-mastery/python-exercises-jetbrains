# MRO Method Resolution Order

## What You'll Learn

Understand Python's Method Resolution Order (MRO), which determines the order in which classes are searched for methods in inheritance hierarchies.

## Concept Overview

When a class inherits from multiple parents, Python needs a consistent way to determine which parent's method to call when there are conflicts. The Method Resolution Order (MRO) is Python's algorithm for deciding this order, ensuring predictable behavior in complex inheritance hierarchies.

Understanding MRO is crucial for debugging multiple inheritance issues and designing class hierarchies correctly.

## Key Concepts

### C3 Linearization

Python uses the C3 linearization algorithm to compute MRO:
- Children come before parents
- Parents are searched left-to-right
- No class appears before its parents

### Viewing MRO

Check a class's MRO using `__mro__` or `mro()`:

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### MRO in Practice

Python searches in MRO order until it finds the method:

```python
class A:
    def method(self):
        return "A"

class B(A):
    pass

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # "C" - B has no method, so continues to C
```

## Example

```python
class Vehicle:
    def capability(self):
        return "Transport"

class LandVehicle(Vehicle):
    def capability(self):
        return "Drive on land"

class WaterVehicle(Vehicle):
    def capability(self):
        return "Travel on water"

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    pass

# Check MRO
print(AmphibiousVehicle.__mro__)
# AmphibiousVehicle -> LandVehicle -> WaterVehicle -> Vehicle -> object

vehicle = AmphibiousVehicle()
print(vehicle.capability())  # "Drive on land" (from LandVehicle)

# MRO searches: AmphibiousVehicle (no method) -> LandVehicle (found!)
```

## Your Task

Explore how Python determines Method Resolution Order in inheritance hierarchies. Use `__mro__` to inspect the search order and understand how conflicts are resolved.
