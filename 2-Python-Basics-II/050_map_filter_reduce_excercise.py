# Use map to print the square of each numbers rounded
# to three decimal places
from functools import reduce

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_square_floats = list(map(lambda number: number ** 2, my_floats))
print(my_square_floats)

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_filtered_names = list(filter(lambda name: len(name) <= 7, my_names))
print(my_filtered_names)

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
my_reduced_numbers = reduce(lambda number1, number2: number1 * number2, my_numbers)
print(my_reduced_numbers)

# Fix all three respectively.
map_result = list(map(lambda x: x ** 2, my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)