# Python Data Types
# List Methods Exercise 2

# Fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']

friends.extend(new_friend)
friends.sort()
print(friends)
