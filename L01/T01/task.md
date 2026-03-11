# Order of Operations

Python follows standard mathematical order when evaluating expressions. Multiplication and division happen before addition and subtraction. When operators have the same priority, Python evaluates from left to right.

**Parentheses override default order**

Operations inside parentheses are always evaluated first:

```python
result = 2 + 3 * 4      # multiplication first: 2 + 12 = 14
result = (2 + 3) * 4    # parentheses first: 5 * 4 = 20
```

**Division operators**

Python has two division operators:
- `/` performs float division and returns a decimal: `7 / 2` → `3.5`
- `//` performs floor division and returns an integer: `7 // 2` → `3`

## Your Task

Complete the arithmetic expressions following the instructions in the comments. Use your understanding of operator precedence and parentheses to create expressions that produce the correct results.

<div class="hint">
Remember: multiplication and division happen before addition and subtraction unless you use parentheses.
</div>
