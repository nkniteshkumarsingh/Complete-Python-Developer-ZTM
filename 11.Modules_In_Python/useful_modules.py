# Modules In Python.
# Useful Modules

from collections import Counter, defaultdict, OrderedDict


li = [1, 2, 3, 4, 5, 6, 5]
sentence = "blah blah blah"
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(
    lambda: 'Key doesn\'t exist.',
    {
        'a': 1,
        'b': 2
    }
)
print(dictionary['a'])
print(dictionary['c'])

d = OrderedDict()
d['a'] = 5
d['b'] = 10

d2 = OrderedDict()
d2['b'] = 10
d2['a'] = 5

d3 = OrderedDict()
d3['a'] = 5
d3['b'] = 10

print(d == d2)
print(d == d3)
