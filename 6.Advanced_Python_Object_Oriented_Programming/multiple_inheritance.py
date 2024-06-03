# Advanced Python: Object-Oriented Programming
# Multiple Inheritance

class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows lef= {self.num_arrows}")

    def check_arrows(self):
        print(f'{self.num_arrows} remaining.')

    def run(self):
        print('Ran really fast.')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('Borgie', 50, 100)
print(hb1.sign_in())
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
