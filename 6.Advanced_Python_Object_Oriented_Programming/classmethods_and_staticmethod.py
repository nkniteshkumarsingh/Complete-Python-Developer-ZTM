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

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Tom', 20)
player2 = PlayerCharacter.adding_things(2, 3)

# print(player1.adding_things(2, 3))
# print(PlayerCharacter.adding_things(3, 5))
print(player2.age)
print(PlayerCharacter.adding_things2(5, 7))
