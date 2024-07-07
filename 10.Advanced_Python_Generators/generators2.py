# Advanced Python: Generators
# Generators2


def generator_function(num):
    for i in range(num):
        yield i*2


g = generator_function(100)
print(next(g))
next(g)
next(g)
print(next(g))
