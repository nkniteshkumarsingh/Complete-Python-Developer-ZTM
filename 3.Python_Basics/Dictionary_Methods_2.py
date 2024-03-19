# Python Data Types
# Dictionary Methods 2

user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 28
}

print('basket' in user)
print('size' in user)
print('age' in user.keys())
print('Hello' in user.values())
print(user.items())

user2 = user.copy()
print(user2)
user2.clear()
print(user2)

print(user.pop('age'))
print(user)
print(user.popitem())
print(user)

user.update({'age': 30})
print(user)
