# Python Data Types
# Dictionary Exercise

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
    'age': 0,
    'username': '',
    'weapon': None,
    'is_active': False,
    'clan': None
}
print(user, '\n')

# 2 iterate and print all the keys in the above user.
print(user.keys(), '\nn')

# 3 Add a new weapon to your user
user['weapon'] = 'Sword'
print(user, '\n')

# 4 Add a new key to include 'is_banned'. Set it to false
user.update(is_banned=False)
print(user, '\n')

# 5 Ban the user by setting the previous key to True
user['is_banned'] = True
print(user, '\n')

# 6 create a new user2 by copying the previous user and update the age value and username value.
user2 = user.copy()
user2['age'] = 28
user2['username'] = 'Nitesh'
print(user2)
