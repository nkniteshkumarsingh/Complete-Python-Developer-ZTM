# Advanced Python: Error Handling
# Error Handling 3

while True:
    try:
        age = int(input('What is your age? '))
        print(age)
        # raise ValueError('hey cut it out.')
        raise Exception('hey cut it out.')

    except ValueError:
        print('Please enter a number.')
