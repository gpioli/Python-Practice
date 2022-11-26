# Reduce
# https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce
# Allows us to pick something and obtain ONE conclusion of that

# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an
# initial argument. It has the following syntax:

# reduce(func, iterable[, initial])



import functools

numbers = [1, 2, 3, 4]
# This will do the running total
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

# Where func is the function on which each element in the iterable gets cumulatively applied to, and initial is the
# optional value that gets placed before the elements of the iterable in the calculation, and serves as a default when
# the iterable is empty. The following should be noted about reduce(): 1. func requires two arguments, the first of
# which is the first element in iterable (if initial is not supplied) and the second element in iterable. If initial
# is supplied, then it becomes the first argument to func and the first element in iterable becomes the second element.
# 2. reduce "reduces" (I know, forgive me) iterable into a single value.

# Let's create our own version of Python buil-in sum() function:

from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, numbers)
print(result)

# same is done here, but with lamba:
result2 = reduce(lambda x, y: x+y, numbers)
print(result2)

# using the optional initial value

result3 = reduce(lambda x, y: x + y, numbers, 10)
print(result3)
