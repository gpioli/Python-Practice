# Maps
# executes a specific function for each element in an iterable
# map(function, iterables)

numbers = [1, 2, 3, 4]

# Old way of applying a transformation
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)
print(numbers)
print(numbers_v2)

# 3 lines vs 1
# numbers_v3 = map(lambda i: i * 2, numbers)
numbers_v3 = map(lambda number: number * 2, numbers)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

# limit here will be the shortest list
# result = map(lambda number1, number2: number1 + number2, numbers_1, numbers_2) if I dont transform the map result to a list,
# the memory direction of the object will be printed instead of the desired result
result = list(map(lambda number1, number2: number1 + number2, numbers_1, numbers_2))
print(result)


package_price = [300, 500, 50]
print(package_price)
passengers = 3
total_price = list(map(lambda price: price * passengers, package_price))
print(total_price)
price_w_taxes = list(map(lambda price: price * 1.22, total_price))
print(price_w_taxes)

# https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce

# Other examples
my_pets = ['alfred', 'tabitha', 'william', 'arla']
print(list(map(str.upper, my_pets)))

# Rounding
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
rounded_areas = list(map(round, circle_areas))
print(rounded_areas)
# The range(1, 7) function acts as the second argument to the round function (the number of required decimal places
# per iteration
increasing_dec_rounded_areas = list(map(round, circle_areas, range(1, 7)))
print(rounded_areas)

# Now we will create our own zip function (zip function is a function that takes a number of iterables and then creates
# a tuple containing each element in iterables).

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
zip_result = zip(my_strings, my_numbers)
print(list((zip_result)))

# Our own zip function:
my_zip = list(map(lambda string, number: (string, number), my_strings, my_numbers))
print(my_zip)

