# File IO
# File Paths

# Relative Path
with open(".\\test_folder\\test2.txt", mode='r') as my_file:
    print(my_file.read(), '\n')

# Absolute Path
with open("D:\Study Zone\Python Codes\Complete-Python-Developer-ZTM\\13.File_IO\\test_folder\\test2.txt") as my_file:
    print(my_file.read())
