# Python Basics II
# While Loops 2

my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input("Say something: ")
    if response == "bye":
        break
