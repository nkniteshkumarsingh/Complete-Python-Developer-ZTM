import re

string = 'My name is Nitesh Kumar Singh. Other name is Nox.'

result = re.search('name', string)
print(result)
print(result.span())
print(result.start())
print(result.end())
print(result.group())


pattern = re.compile('name')
value1 = pattern.search(string)
value2 = pattern.findall(string)
value3 = pattern.fullmatch(string)
value4 = pattern.match(string)

print(value1)
print(value2)
print(value3)
print(value4)
