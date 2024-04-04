# Python Basics II
# Logical Operators Exercise

is_magician = True
is_expert = False

# Check if magician and expert: "You are a master magician."
if is_magician and is_expert:
    print("You are a master magician.")

# Check if magician but not expert: "At least you're getting there."
elif is_magician and not is_expert:
    print("At least you're getting there.")

# Check if not a magician: "You need magic powers."
elif not is_magician:
    print("You need magic powers.")
