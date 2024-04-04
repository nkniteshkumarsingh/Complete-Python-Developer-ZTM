# Python Basics II
# Iterables

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)

# for item in user:
#     print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)
