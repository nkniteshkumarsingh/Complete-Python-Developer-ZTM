# Advanced Programming: Functional Programming
# map, filter, zip, reduce exercises

from functools import reduce


# 1 Capitalize all the pet names and print the list
def capitalize(name):
    return name.capitalize()


my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
def pass_over_50(score):
    return score > 50


scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(pass_over_50, scores)))


# 4 Combine all the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_numbers + scores))
