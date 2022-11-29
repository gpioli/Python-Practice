# We are going to work with files
# https://realpython.com/working-with-files-in-python/

file = open("023_text_file.txt")
# This will read all the text in the text file | If it's a big file, the memory consumption will be high
# print(file.read())

# But we can also read line by line: | This method is lighter than the previous one
print(file.readline())
print(file.readline())
print(file.readline())

# Closing the file => very important
file.close()

# Another way: | This has the best of both worlds: low memory consumption and knows when to stop reading
file = open("023_text_file.txt")
for line in file:
    print(line)
file.close()

# Something very important is to close the opened file once finished the operation | This can be done with the following
# instruction: (opens the file and closes it once finished doing the requested operations
with open("023_text_file.txt") as file:
    for line in file:
        print(line)

