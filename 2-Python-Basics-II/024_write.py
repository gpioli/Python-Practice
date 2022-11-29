# This will not work, as by defect we work with read permits:
# with open("./023_text_file.txt", "r") as file:
#     for line in file:
#         print(line)
#     file.write("new things in this file")

# with r+ permit we can add new content
with open("./023_text_file.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("\n new things in this file.")
    file.write("\n and some more things.")

with open("./023_text_file.txt") as file:
    for line in file:
        print(line)

# with w+ permit we can read the file, but all the content in the file will be overwritten:
with open("./023_text_file.txt", "w+") as file:
    for line in file:
        print(line)
    file.write("\n new things in this file.")
    file.write("\n and some more things.")
