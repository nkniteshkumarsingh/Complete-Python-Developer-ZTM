import re

pattern = re.compile(r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$")

string1 = "nkniteshkumarsingh@gmail.com"
string2 = "niteshkumar"

isemail1 = pattern.search(string1)
isemail2 = pattern.search(string2)

print(isemail1)
print(isemail2)
