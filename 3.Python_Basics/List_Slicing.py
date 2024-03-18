# Python Data Types
# List Slicing
# list[start: stop: stepover]

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])
print(amazon_cart[::-1])
amazon_cart[0] = 'laptop'
print(amazon_cart[1:3])
print(amazon_cart)
