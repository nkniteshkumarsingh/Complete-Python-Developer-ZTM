# Python Data Types
# Common List Patterns

basket = ["a", "x", "b", "c", "d", "e", "d"]
print(basket)
print(len(basket), "\n")

basket.sort()
print(basket)

print(basket[::-1])
print(basket)

basket.reverse()
print(basket, "\n")

print(range(1, 100))
print(list(range(1, 10)))
print(list(range(11)), "\n")

# sentence = "! "
# new_sentence = sentence.join(["Hi", "My", "name", "is", "Nitesh"])
# print(new_sentence)

sentence = "! ".join(["Hi", "My", "name", "is", "Nitesh"])
print(sentence)
