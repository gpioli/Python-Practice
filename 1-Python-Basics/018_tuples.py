# Working with tuples (inmutable element)

numbers = (1, 2, 3, 4, 5)
print(type(numbers))

strings = ("nick", "riley", "francis")
print(type(strings))

# Accessing the elements in the tuple:
print("Element 0 =>", numbers[0])
print("Last element  =>", numbers[-1])

### In tuples we cant apply the same actions we applied over lists (because of their inmutable
# nature)

#numbers.append(2) #This breaks: 'tuple' object has no attribute 'append'

print(strings)
print(strings.index("riley"))
print(strings.count("nick"))

# Converting a tuple to list:
my_list = list(strings)
print(my_list)
my_list[1] = "Billie"
print(my_list)

# Now we can go back to a tuple:
my_tuple = tuple(my_list)
print(my_tuple)