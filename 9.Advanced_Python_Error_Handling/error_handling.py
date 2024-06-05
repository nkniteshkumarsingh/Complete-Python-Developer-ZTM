# Advanced Python: Error Handling
# Error Handling

while True:
    try:
        age = int(input('What is your age? '))
        print(age)

    except ValueError:
        print('Please enter a number.')

    except ZeroDivisionError:
        print('Please enter age higher than 0.')

    else:
        print('Thank you!')
        break
