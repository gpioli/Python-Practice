# Working with lists
# A list is analog to an Array in Java


numbers = [1, 2, 3, 4]
print(numbers, type(numbers))

tasks = ["do the dishes", "make the bed", "prepare dinner"]
print(tasks)

types = [1, True, "Hello!"] # Lists can contain different type of data

print(numbers[0])
print(tasks[0])

text = "Hello!"
print(text[0])

################################################
# Strings are inmutables, but lists are mutable#
################################################


#text[0] = "W" # this will break | TypeError: 'str' object does not support item assignment
# print(text) #

print(tasks)
tasks[0] = "watch tv and play videogames"
print(tasks)

print(numbers[:3])

print(True in types) # this will return True
print("Hello!" in types) # this will return True

