# Sets Exercise

## Theory

In this task you will practice set methods that modify a set or compare two sets.

`set.add(value)` adds one element to a set. If the value is already there, nothing changes.

`set.discard(value)` removes an element from a set. If the value is not in the set, it does not raise an error.

`set.difference_update(other)` removes from the set all elements that are also found in `other`. This changes the set in place (no new set is created).

`set.issubset(other)` returns `True` if every element of the set is contained in `other`.

`set.issuperset(other)` returns `True` if the set contains every element of `other`.
