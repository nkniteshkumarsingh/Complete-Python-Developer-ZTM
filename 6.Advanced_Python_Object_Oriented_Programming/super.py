# Advanced Python: Object-Oriented Programming
# Super

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
wizard1.sign_in()
print(wizard1.email)
