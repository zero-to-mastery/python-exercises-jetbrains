# Cats Everywhere
# Complete the code below

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create three Cat instances
cat1 = Cat('Whiskers', 5)
cat2 = Cat('Mittens', 1)
cat3 = Cat('Shadow', 8)


# Complete the function to return the oldest cat age
def oldest_cat(*args):
    return max(args)


# Store the oldest cat age in answer
oldest_age = oldest_cat(cat1.age, cat2.age, cat3.age)
