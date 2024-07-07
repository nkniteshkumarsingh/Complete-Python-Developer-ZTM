# Advanced Python: Generators
# Fibonacci Numbers Exercise
# Write a function to implement Fibonacci numbers using generators.


def fib(number):
    first = 0
    second = 1
    for i in range(number):
        yield first
        temp = first
        first = second
        second += temp


for x in fib(21):
    print(x)


# def fib2(number):
#     first = 0
#     second = 1
#     result = []
#     for i in range(number):
#         result.append(first)
#         temp = first
#         first = second
#         second += temp
#     return result
#
#
# print(fib2(21))
