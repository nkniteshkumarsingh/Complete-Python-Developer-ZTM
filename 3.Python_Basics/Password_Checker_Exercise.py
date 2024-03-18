# Python Data Types
# Password Checker Exercise
# Input username and password and print “Password is --- length long”.

username = input("Enter your username:\t")
password = input("Enter your password:\t")

password_length = len(password)
masked_password = password_length * "*"

print(f"Hey {username}! Your password {masked_password} is {password_length} characters long.")
