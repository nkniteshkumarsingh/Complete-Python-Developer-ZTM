# Advanced Programming: Functional Programming
# filter()

my_list = [1, 2, 3]


def only_odd(item):
    return item % 2


print(list(filter(only_odd, my_list)))
print(my_list)
