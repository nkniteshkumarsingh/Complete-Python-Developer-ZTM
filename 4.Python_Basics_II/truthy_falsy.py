# Python Basics II
# Truthy and Falsy

print(bool("Hello"))
print(bool(3))
print(bool(''))
print(bool(0))
print(bool(None))

username = "Nitesh"
password = "123"

if username and password:
    print(f"Hello {username}! Please enter your password to login: ")
