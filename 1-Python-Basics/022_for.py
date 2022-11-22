### Working with for cycle

print("First iteration")
for element in range(20):
    print(element) # Will print all elements in range 0-19

print("Second iteration")
# another way of writing the same:
for element in range(1,20):
    print(element)

print("Third iteration - list")
# looping through a list:
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element) # will print all the elements

print("Fourth iteration - tuple")
my_tuple = ("nick", "jamie", "mia")
for element in my_tuple:
    print(element)

product = {
    "name": "shirt",
    "price": 200,
    "stock": 20
}

print("Fifth iteration - dict")
for element in product:
    print(element) # iterates over the keys

for element in product:
    print(product[element])

# Another way:
for key, value in product.items(): ### this returns an array with tuples (key, value),
    print(key, "=> ", value)

### This is what is more usually seen in development world:
# A list/array of dictionaries

people = [
    {
        "name" : "nick",
        "age": 34
    },
    {
        "name": "ian",
        "age": 23
    },
    {
        "name": "mery",
        "age": 27
    }

]

for person in people:
    print(person)

for person in people:
    print("name =>", person["name"])