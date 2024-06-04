# Advanced Python: Decorators
# Higher Order Functions

def greet(func):
    return func()


def greet2():
    def func():
        return 5
    return func
