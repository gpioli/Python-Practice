# Working with filter

# While map() passes each element in the iterable through a function and returns the result of all elements having
# passed through the function, filter(), first of all, requires the function to return boolean values (true or false)
# and then passes each element in the iterable through the function, "filtering" away those that are false.
# It has the following syntax:

# filter(func, iterable)

numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # I am filtering even elements inside of the array
print(new_numbers)
print(numbers)

# Filter doesn't alter the original state of the objects, just like map

# More examples:
# https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce

# The following points are to be noted regarding filter():

# - Unlike map(), only one iterable is required.
# - The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed
#  to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
# - filter passes each element in the iterable through func and returns only the ones that evaluate to true.
# I mean, it's right there in the name -- a "filter".

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# Lets filter those who passed with scores more than 75:
filtered_scores = list(filter(lambda x: x > 75, scores))
print(filtered_scores)

# The next example will be a palindrome detector. A "palindrome" is a word, phrase, or sequence that reads the same
# backwards as forwards. Let's filter out words that are palindromes from a tuple (iterable) of suspected palindromes.

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)