# Advanced Python: Decorators
# Decorator 2

def my_decorator(func):
    def wrap_func():
        print('*' * 10)
        func()
        print('*' * 10)
    return wrap_func


@my_decorator
def hello():
    print('hellllooooo')


@my_decorator
def bye():
    print('see ya later')


hello()
bye()
