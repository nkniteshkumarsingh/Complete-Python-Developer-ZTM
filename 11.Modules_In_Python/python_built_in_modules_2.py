# Modules In Python.
# Python Built-in Modules 2

import sys

try:
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    print(f"Hellooo! {first_name} {last_name}.")

except IndexError as err:
    print("Please enter you first and last name.")
