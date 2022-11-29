# Working with errors
# https://www.w3schools.com/python/python_ref_exceptions.asp

# Syntax error:
# print(0 / 0))

# ZeroDivisionError:
# print(0 / 0)

# NameError
# print(variable)

# AssertionError
# sum_1 = lambda x, y: x + y
# assert sum_1(1, 2) == 4


# Creating our own errors:
age = 10
if age < 18:
    raise Exception("Under age not allowed")

#

