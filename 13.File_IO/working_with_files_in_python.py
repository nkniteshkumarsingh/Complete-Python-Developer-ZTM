# File IO
# Working with files in Python

my_file = open("test.txt")
print(my_file)
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read(), '\n')

my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
print(my_file.readline(), '\n')

my_file.seek(0)
print(my_file.readlines())

my_file.close()
