# Python Data Types
# List Methods 3

basket = ["a", "x", "b", "c", "d", "e", "c", "d"]
print(basket)

# Built-in function sorted()
# print(sorted(basket))
# print(basket)

new_basket = basket.copy()
print(new_basket)

basket.reverse()
print(basket)

# basket.sort()
# basket.reverse()
# print(basket)

basket.sort(reverse=True)
print(basket)

basket.sort()
print(basket)
