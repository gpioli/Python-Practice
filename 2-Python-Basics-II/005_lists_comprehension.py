# https://www.w3schools.com/python/python_lists_comprehension.asp

# classic way
numbers = []
for element in range(1,11):
    numbers.append(element)
print(numbers)

# list comprehension
numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)


# modfication
numbers = []
for element in range(1,11):
    numbers.append(element * 2)
print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)

# adding elements that satisfy a condition
print('adding elements that satisfy a condition')

# Classic way
even_numbers_x2 = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers_x2.append(i * 2)
print(even_numbers_x2)

# List comprehension
even_numbers_x2_v2 = [i*2 for i in range(1, 11) if i % 2 == 0]
print(even_numbers_x2_v2)



big_list = [element for element in range(1, 100) if element <= 25]
print(big_list)