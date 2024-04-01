# Debugging in Python

import pdb


def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    print(t)
    return num1 + num2


# print(add(5, 'dshafjkl'))
print(add(3, 5))
