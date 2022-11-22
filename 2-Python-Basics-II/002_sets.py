#  Set properties:
# - Can be modified
# - Don't have an order
# - Don't allow duplicated


# Notice it starts as a dictionary {} but it only has values, not keys.

# sets can contain any data type:

# Strings
set_countries = {'Colombia', 'Mexico', 'Bolivia'}
print(set_countries)
print(type(set_countries))

# Numbers
set_numbers = {1, 2, 3, 443, 25}
print(set_numbers)

# Mix both, or even have boolean
set_types = {1, 'hola', False, 12.2}
print(set_types)

# Creating sets from other data structures -> Implicitly:
set_from_strings = set('Hello')
print(set_from_strings)  # Notice elements do not repeat

set_from_tuples = set(('abc', 'cbd', 'as'))
print(set_from_tuples)

numbers = [1,2,3,4,4,4,6,7,9,9,10,2,8]
set_numbers = set(numbers)
print(set_numbers)