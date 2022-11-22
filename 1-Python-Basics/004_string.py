# strings practice

name = "Leroy"
last_name = "Jenkins"

print(name)
print(last_name)

# Concatenation in python
full_name = name + " " + last_name
print(full_name)

# inserting special characters: if we declare the string with "", we can add inside
# <'> without a problem
# But if we declared string with '', if we inserted ' inside there will be a problem with this.
# Solution:
quote = "She said \"hello\" "
print(quote)

quote2 = "I'm Gaston"
print(quote2)

# Using format for printing
template = "Hi, my name is " + name + " and my last name is " + last_name
print(template)

template_v2 = "Hi, my name is {} and my last name is {}".format(name, last_name)
print(template_v2)

# f-Strings:
template_v3 = f"Hi, my name is {name} and my last name is {last_name}"
print(template_v3)

# Challenge:
print("")
print("----Starts program execution----")
user_name = input("Please, enter your name: ")
user_age = input("What's your age? ")
print(f"Hi, {user_name}! Next year you'll be turning {int(user_age) +1}")
