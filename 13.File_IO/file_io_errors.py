# File IO
# File IO Errors

try:
    with open("test3.txt", mode='r') as my_file:
        print(my_file.read())

except FileNotFoundError as err:
    print("File doesn't exist.")
    raise err

except IOError as err:
    print("IO Error")
    raise err
