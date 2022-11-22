# We continue working with dictionaries

# https://www.w3schools.com/python/python_dictionaries_methods.asp

person = {
    "name" : "John",
    "last_name" : "Snow",
    "langs": ["dothraki", "high valyrian", "low valyrian"],
    "age": 17
}

print(person)
print(person["name"])

# Updating values:

person["name"] = "Tyrion"
person["age"] = 25
person["langs"].append("lhazar")
print(person)

# deleting values
del person["last_name"]
print(person)

person["last_name"] = "lannister"
print(person)

# in dictionaries, pop method should contain the key we want to delete or pop
person.pop("age")
print(person)

print(person.items()) # prints in an array(list) tuples  that contains key-value
print(person.keys())
print(person.values())