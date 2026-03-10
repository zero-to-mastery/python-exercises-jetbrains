# Working With Sets

## Theory

A **set** (`set`) is a collection that stores **unique** values. That means duplicates are removed automatically. Sets are great when you need to quickly check “is this value present?” or when you want to compare groups of items (for example: who is in the school database vs who was present today).

## Difference

One of the most useful set operations is **difference**.

`A.difference(B)` returns a **new set** with all elements that are in `A` but **not** in `B`.
So it answers the question: “Who/what is missing from `B`, compared to `A`?”

`difference()` does not require `B` to be a set. The second argument can be any **iterable** (like a list or tuple). Python will compare the values and return the missing ones.

## Intersection

Another useful operation is **intersection**.

`A.intersection(B)` returns a **new set** with elements that appear in **both** `A` and `B`.
This answers: “Who/what is included in both groups?”

## Union

You can also combine groups using **union**.

`A.union(B)` returns a **new set** with **all unique** elements from `A` and `B`.
This answers: “What are all the unique names/items we have in total?”

## Disjoint

Finally, `A.isdisjoint(B)` checks if two collections have **no elements in common**.
It returns `True` if they do not overlap at all, and `False` if they share at least one value.

Just like `difference()`, these methods (`intersection`, `union`, `isdisjoint`) can take any **iterable** as the second argument.
