# Advanced Programming: Functional Programming
# Exercise Comprehensions

# Return a list of duplicates in the given list.
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({x for x in some_list if some_list.count(x) > 1})
print(duplicates)
