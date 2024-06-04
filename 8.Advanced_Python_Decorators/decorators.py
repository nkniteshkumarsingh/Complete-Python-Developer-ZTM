# Advanced Python: Decorators
# Decorator

def hello(func):
    return func()


def greet():
    print('still here!')


a = hello(greet)
print(a)
