# Python Basics II
# Break, Continue, Pass

my_list = [1, 2, 3]

for item in my_list:
    break
    print(item)

for item in my_list:
    continue
    print(item)

for item in my_list:
    pass

i = 0
while i < len(my_list):
    i += 1
    break
    print(my_list[i])

i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass
