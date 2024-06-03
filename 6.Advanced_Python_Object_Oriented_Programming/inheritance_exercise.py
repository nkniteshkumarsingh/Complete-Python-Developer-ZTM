# Advanced Python: Object-Oriented Programming
# Inheritance Exercise

class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around.'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class Chilly(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all the pets (create 3 cat instances from the above)
my_cats = []
cat1 = Simon('Simon', 5)
cat2 = Sally('Sally', 7)
cat3 = Chilly('Chilly', 3)

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all the cats walking using the my_pets instance
my_pets.walk()
