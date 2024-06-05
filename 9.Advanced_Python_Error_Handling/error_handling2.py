# Advanced Python: Error Handling
# Error Handling 2

def sum_(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers. {err}')


print(sum_(1, '2'))
