# Advanced Python: Object-Oriented Programming
# Attributes and Methods

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")

    def run(self, hello):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 50

# help(player1)
print(player2.membership)
print(player1.shout())
print(player2.shout())
