# For Loop Counter

## What Is a Counter Pattern?

A counter (or accumulator) is a variable that collects values as you loop through data. It's one of the most common patterns in programming.

## The Pattern

```python
total = 0                # 1. Initialize
for num in numbers:      # 2. Loop through items
    total += num         # 3. Accumulate
```

## Augmented Assignment

The `+=` operator adds and assigns in one step:

```python
count = 0
count += 5   # Same as: count = count + 5
count += 3   # count is now 8
```

Other augmented operators: `-=`, `*=`, `/=`

<div class="hint">
Use the augmented assignment operator `+=` to add each item to the counter.
</div>
