# Dictionaries and Dictionary Methods

## What You'll Learn

How to create and manipulate dictionaries using key-value pairs and explore the methods available for working with dictionary data.

## Concept Overview

Dictionaries are Python's mapping type, storing data as key-value pairs. Unlike sequences that use numeric indices, dictionaries use keys (which can be strings, numbers, or other immutable types) to access values. This makes them ideal for representing structured data, configuration settings, or any scenario where you need to look up values by meaningful labels.

Dictionaries are mutable and unordered (though Python 3.7+ preserves insertion order). They provide numerous methods for accessing, modifying, and querying their contents efficiently.

## Key Concepts

### Key-Value Pairs

Dictionaries store associations between keys and values. Each key must be unique and immutable (strings, numbers, tuples), while values can be any type, including lists or other dictionaries. You access values using square bracket notation with the key.

### Dictionary Methods

Dictionaries provide methods like `get()` for safe access (returns a default if key doesn't exist), `keys()` and `values()` for iterating, `items()` for getting key-value pairs, `update()` for merging dictionaries, `pop()` and `popitem()` for removing items, and `copy()` for creating duplicates.

### Membership Testing

The `in` operator checks if a key exists in the dictionary. By default, it checks keys, but you can also test membership in `keys()`, `values()`, or `items()` explicitly.

## Example

```python
# Creating a dictionary
product = {
    'name': 'Laptop',
    'price': 999.99,
    'in_stock': True,
    'specs': ['16GB RAM', '512GB SSD']
}

# Accessing values
print(product['name'])  # Laptop
print(product.get('discount', 0))  # 0 (default value)

# Checking membership
print('price' in product)  # True
print(999.99 in product.values())  # True

# Getting keys, values, and items
print(product.keys())  # dict_keys(['name', 'price', 'in_stock', 'specs'])
print(product.items())  # dict_items([...])

# Modifying
product.update({'discount': 10})
product['price'] = 899.99

# Copying
new_product = product.copy()
```

## Your Task

You'll practice creating dictionaries, accessing values with indexing and the get() method, using membership tests, and applying various dictionary methods to manipulate and query dictionary data.
