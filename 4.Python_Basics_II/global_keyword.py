# Python Basics II
# Global Keyword

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())


# def count(total):
#     total += 1
#     return total
#
#
# print(count(count(count(total))))
