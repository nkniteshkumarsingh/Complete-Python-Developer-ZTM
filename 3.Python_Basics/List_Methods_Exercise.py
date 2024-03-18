# Python Data Types
# List Methods Exercise


# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket, "\n")

# 1. Remove the Banana from the list
basket.remove("Banana")
print(basket, "\n")

# 2. Remove "Blueberries" from the list.
basket.pop()
print(basket, "\n")

# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
print(basket, "\n")

# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
print(basket, "\n")

# 5. Count how many apples in the basket
print(basket.count("Apples"), "\n")

# 6. empty the basket
basket.clear()
print(basket)
