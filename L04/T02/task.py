# Pets Everywhere
# Complete the code below

class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        result = []
        for animal in self.animals:
            result.append(animal.walk())
        return result


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Add another Cat class named `Chilli` and implement the `sing` method
class Chilli(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Create 3 cat instances
cat1 = Simon('Simon', 5)
cat2 = Sally('Sally', 7)
cat3 = Chilli('Chilli', 3)


# Create a Pets instance
my_cats = [cat1, cat2, cat3]
my_pets = Pets(my_cats)

# Store the walking results in answer
answer = my_pets.walk()