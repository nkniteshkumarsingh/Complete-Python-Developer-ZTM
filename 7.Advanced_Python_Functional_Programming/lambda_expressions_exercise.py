# Advanced Programming: Functional Programming
# Exercise Lambda Expressions

my_list = [5, 4, 3]
# Create a lambda expression which will square the list items.
print(list(map(lambda x: x**2, my_list)))

a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
