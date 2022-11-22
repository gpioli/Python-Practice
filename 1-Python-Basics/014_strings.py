### Working with Strings

# https://www.w3schools.com/python/python_strings_methods.asp

text = "She knows how to program in Python"

print('JavaScript' in text) # False
print('Python' in text) # True

if 'JS' in text:
    print("You choosed wisely!")
else: print("Python is an awesome programming language!") # This prints

size = len(text)
print(size) #34


print(text, text.upper()) # Prints the text, and then the text in uppercase
print(text.lower()) # Prints the text, and then the text in uppercase

print(text.count('a')) # returns 1
print(text.swapcase()) # swaps uppercase to lowercase and vice versa

print(text.endswith('Rust')) # False
print(text.replace('Python', 'Go'))

text_2 = "this is a title"
print(text_2)
print(text_2.capitalize()) # Turns the first character to uppercase
print(text_2.title()) # Turns each first character in a string to uppercase

print(text_2.isdigit()) # tells us if the string is a digit # returns False
text_3 = "182"
print(text_3.isdigit()) # Returns True

