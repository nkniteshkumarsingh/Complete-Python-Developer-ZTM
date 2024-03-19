# Python Data Types
# Tuples 2

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[1:2]

print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(other)
print(z)

# Tuple Methods
print(my_tuple.count(3))
print(my_tuple.index(3))
print(len(my_tuple))
