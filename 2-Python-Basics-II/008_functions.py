# https://www.w3schools.com/python/python_functions.asp

# functions allow code reuse and avoid repetition
# also makes it easier to maintain code over time

# we have already worked with functions:
print("Hello")

# creating functions
def my_print():
    print("This is my print")

my_print()


# Creating a function that receives parameters:
def my_print_with_params(text):
    print("Hello,", text)

my_print_with_params("Gaston")

#
a = 10
b = 90

# this doesn't scale
c = a + b


def suma(x, y):
    print(x + y)  # this functions has two responsibilities: summing and printing


suma(10, 5)
