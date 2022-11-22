### CRUD - CREATE, READ, UPDATE & DELETE


#CREATE
numbers_list = [1, 2, 3, 4, 5]

#READ
print(numbers_list[0])

#UPDATE
numbers_list[-1] = 100 # replaces last element
print(numbers_list)

numbers_list.append(200) # insterts an element in the final place
print(numbers_list)

numbers_list.insert(0, "hello")
print(numbers_list) # insterts an element in the specified position

numbers_list.insert(3, "change")
print(numbers_list)

tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers_list + tasks
print(new_list)

print(new_list.index("todo 2")) # prints the index were the element is located

index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

# DELETE
new_list.remove("todo 1") # deletes the specified element
print(new_list)

new_list.pop() # deletes the last element
print(new_list)

new_list.pop(0) # we can send a parameter of the position we want to delete
print(new_list)

# reversing the order of the list
new_list.reverse()
print(new_list)

# Sorting:
numbers_a = [1, 4, 2, 9]
numbers_a.sort()
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)

# sort only works if the data type is homogeneus


