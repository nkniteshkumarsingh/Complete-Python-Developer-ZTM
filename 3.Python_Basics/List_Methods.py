# Python Data Types
# List Methods

basket = [1, 2, 3, 4, 5]

print(basket, "\n")

# Adding
basket.append(100)
print(basket)

basket.insert(4, 250)
print(basket)

basket.extend([300, 400, 500])
print(basket, "\n")

# Removing
print(basket.pop())
print(basket)

basket.remove(400)
print(basket)

basket.clear()
print(basket)
