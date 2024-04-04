# Python Basics II
# Functions Exercise

# Highest Even: Write a function to find the highest even number from the list.

def highest_even(li):
    value = 0
    for item in li:
        if value < item and not item % 2:
            value = item
    return value


print(highest_even([1, 2, 3, 10, 4, 8, 15]))
