# Python Data Types
# Formatted Strings

name = "Nitesh"
age = 27

print("Hi " + name + "! You are " + str(age) + " years old.\n")

# Python 3 formatted strings
print(f"Hi {name}! You are {age} years old.\n")

# Python 2 formatted strings
print("Hi {}! You are {} years old.".format(name, age))
print("Hi {1}! You are {0} years old.".format(age, name))
print("Hi {new_name}! You are {age} years old.".format(new_name="Sally", age=100))
