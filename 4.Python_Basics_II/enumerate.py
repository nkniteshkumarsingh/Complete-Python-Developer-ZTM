# Python Basics II
# Enumerate

for i, char in enumerate("Helllooo"):
    print(i, char)

for i, num in enumerate([1, 2, 3]):
    print(i, num)

for i, num in enumerate((1, 2, 3)):
    print(i, num)

for i, num in enumerate(list(range(100))):
    if num == 50:
        print(f"Index of {num} is {i}.")
