# File IO
# Read, Write, Append

with open('test.txt') as my_file:
    print(my_file.readlines(), '\n')


with open('test.txt', mode='a') as my_file:
    text2 = my_file.write("\n;)")
    print(text2)

with open('test.txt', mode='r') as my_file:
    print(my_file.readlines(), '\n')


with open('test.txt', mode='r+') as my_file:
    text = my_file.write("Hey! It\'s me.")
    print(text)

with open('test.txt', mode='r') as my_file:
    print(my_file.readlines(), '\n')


with open('test.txt', mode='w') as my_file:
    text3 = my_file.write("Hi! My name is Nitesh Kumar.\n:)\nHow are you?")
    print(text3)

with open('test.txt', mode='r') as my_file:
    print(my_file.readlines(), '\n')

#
# with open('test2.txt', mode='w') as my_file:
#     text4 = my_file.write("hey! What's up?")
#     print(text4)
#
# with open('test2.txt', mode='r') as my_file:
#     print(my_file.readlines(), '\n')
