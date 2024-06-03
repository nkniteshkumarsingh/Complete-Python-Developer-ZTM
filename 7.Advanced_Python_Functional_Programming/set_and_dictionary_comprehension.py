# Advanced Programming: Functional Programming
# List Comprehensions

my_set = {char for char in 'hello'}
print(my_set)

my_set2 = {num for num in range(0, 100)}
print(my_set2)

my_set3 = {num*2 for num in range(0, 100)}
print(my_set3)

my_sdt4 = {num**2 for num in range(0, 100) if not num % 2}
print(my_sdt4)

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in simple_dict.items()}
print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)
