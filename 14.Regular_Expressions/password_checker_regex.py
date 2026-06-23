# Password must:
# be atleast 8 characters long
# contains letters, numbers and $%#@
# ends with a number

import re

pattern = re.compile(r"^(?=.*[\w])(?=.*[$%#@]+).{7,}\d$")

password = 'qwerty$#%67439'

check = pattern.fullmatch(password)
print(check)
