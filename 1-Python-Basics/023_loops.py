# working with loops

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#printing elements inside the list of lists
print(matrix[0][1])

for element in matrix:
    print(element)

# iterating through sublists
for element in matrix:
    for subelement in element:
        print(subelement)

