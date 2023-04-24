# Exercise Common List Patterns
# Fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)
friends.sort()
print(friends)
