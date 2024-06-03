# Advanced Python: Object-Oriented Programming
# __init__

class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 10)

print(player1.shout())
# print(player2.shout())
