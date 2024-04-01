# Modules In Python.
# Python Built-in Modules

import random as rd

print(rd)
# help(rd)
# print(dir(rd))
print(rd.random())
print(rd.randint(1, 27))
print(rd.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
rd.shuffle(my_list)
print(my_list)
