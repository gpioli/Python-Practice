# Working with modules
# https://www.w3schools.com/python/python_modules.asp
# Consider a module to be the same as a code library.
#
# A file containing a set of functions you want to include in your application.


import sys

print(sys.path)

import re

text = "My telephone number is 311 123 121, and the country code is 44. My lucky number is 18"

# Find everything that is a number
result = re.findall("[0-9]+", text)
print(result)

# Module for times and dates

import time

timestamp = time.time()
local = time.localtime()
result_time = time.asctime(local)
print(timestamp)
print(result_time)

# Module for working with lists

import collections

numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers) # returns a dict with the repetition
print(counter)
