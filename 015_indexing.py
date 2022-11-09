# Working with indexing and slicing

text = "She knows Python"
print(text[0]) # Prints the first char
print(text[1])

print("\n")

for i in range(0, len(text)):
    print(text[i])

print("")

size = (len(text))
print(text[size-1]) # we dont have to extract -1 as python goes
print(text[-1]) # this does the same

# slicing:

print(text[0:5]) # 5 is not included
print(text[:10]) # from the beginning to the 9th char
print(text[5:-1]) # Starts at 5 and finishes one character before the last one
print(text[:]) # prints everythin

print(text[10:16:2]) # Goes from the char 10 to the 15, skipping one character
