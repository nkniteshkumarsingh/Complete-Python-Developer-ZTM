# Python Basics II
# Default Parameters and Keyword Arguments

# Parameters
def say_hello(name, emoji):
    print(f"Helllooooo {name} {emoji}")


# Positional Arguments
say_hello("Nitesh", ":)")


# Default Parameters
def say_hello2(name = "Darth Vader", emoji = ">:("):
    print(f"Helllooooo {name} {emoji}")


# Positional Arguments
say_hello2("Nitesh", ":)")
say_hello2()

# Keyword Arguments
say_hello2(emoji=":)", name="Nitesh")
say_hello2(name="Nitesh")
say_hello2(emoji=":)")
