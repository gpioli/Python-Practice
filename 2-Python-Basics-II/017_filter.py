# Working with filter

numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # I am filtering even elements inside of the array
print(new_numbers)
print(numbers)

# Filter doesn't alter the original state of the objects, just like map

