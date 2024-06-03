# Advanced Python: Object-Oriented Programming
# Encapsulation

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


player1 = PlayerCharacter('Nitesh', 27)
player1.speak()
