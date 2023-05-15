# Exercise Tesla

# age = input("What is your age?: ")
#
# if int(age) < 18:
#     print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
#     print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
#     print("Congratulations on your first year of driving. Enjoy the ride!")
#
# 1. Wrap the above code in a function called checkDriverAge().
# Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
#
# 2. Instead of using the input().
# Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.


def check_driver_age(age=0):
    if age < 18:
        text = "Sorry, you are too young to drive this car. Powering off!"
    elif age > 18:
        text = "Powering On. Enjoy the ride!"
    else:
        text = "Congratulations on your first year of driving. Enjoy the ride!"
    return text


driver1 = check_driver_age()
driver2 = check_driver_age(92)
driver3 = check_driver_age(18)
print(driver1)
print()
print(driver2)
print()
print(driver3)
