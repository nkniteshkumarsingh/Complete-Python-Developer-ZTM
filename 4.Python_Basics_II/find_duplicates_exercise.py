# Python Basics II
# Find Duplicates Exercise

# Check for duplicates in the list.
# Print the characters which have duplicates in the list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

# for i in range(len(some_list)):
#     j = i + 1
#     while j < len(some_list):
#         if some_list[i] == some_list[j] and some_list[i] not in duplicates:
#             duplicates.append(some_list[i])
#         j += 1
#
# print(duplicates)


for value in some_list:
    if some_list.count(value) > 1 and value not in duplicates:
        duplicates.append(value)

print(duplicates)
