# Advanced Python: Decorators
# Decorator 3

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*' * 10)
        func(*args, **kwargs)
        print('*' * 10)
    return wrap_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('Hiiiii', '>:(')
hello('Hi')
