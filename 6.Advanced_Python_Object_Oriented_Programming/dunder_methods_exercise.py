# Advanced Python: Object-Oriented Programming
# Dunder Methods

# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.

class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return 'yes??'

    def __getitem__(self, i):
        return self.my_dict[i]

    def __bool__(self):
        return 'This is bool method.'

    def __add__(self, other):
        return f'added {other}.'

    def __copy__(self):
        return 'Done copying.'


action_figure = Toy('red', 0)
print(action_figure.__bool__())
print(action_figure.__add__(5))
print(action_figure.__copy__())
