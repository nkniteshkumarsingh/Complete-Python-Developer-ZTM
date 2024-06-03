# Advanced Programming: Functional Programming
# List Comprehensions

my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num for num in range(0, 100)]
print(my_list2)

my_list3 = [num*2 for num in range(0, 100)]
print(my_list3)

my_list4 = [num**2 for num in range(0, 100) if not num % 2]
print(my_list4)
