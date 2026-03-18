# Generators
# Complete the code below

# Create a generator function called fib(number).
# It should yield Fibonacci numbers starting from 0.

def fib(number):
    n1 = 0
    n2 = 1
    for i in range(number):
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2
