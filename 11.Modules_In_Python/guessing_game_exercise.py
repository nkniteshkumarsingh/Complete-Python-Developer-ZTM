# Modules In Python.
# Guessing Game Exercise

from sys import argv
from random import randint

try:
    start = int(argv[1])
    end = int(argv[2])
    result = randint(start, end)
    guess = int(input(f"Guess the number between {start} and {end}: "))
    attempts = 1
    while guess != result:
        attempts += 1
        if guess < start or guess > end:
            print(f"Please guess the number between {start} and {end}. Not beyond limits.")
        guess = int(input("Not the number! Try again: "))
    else:
        print(f"Bravo! You guessed the number {result} in {attempts} attempts.")

except IndexError as err:
    print("Please enter start and end numbers to start guessing.")

except ValueError as err:
    print("You are supposed to enter start and end numbers to start guessing.")
