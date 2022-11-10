# Working with dictionaries (another data structure)


my_dict = {}
print(type(my_dict)) #<class 'dict'>


# formed by Key (usually a string), and value pairs:
my_dict = {
    "airplane model": "737",
    "airline": "Air France",
    "country": "France"
}

print(my_dict)
print(len(my_dict)) # 3 elements key-value

# getting values from the dic: (if the value does not exist, Python will explode'
print(my_dict["airplane model"])
print(my_dict["airline"])

# Python can handle this way none existing values in the dict, returning a 'None' if we
# use <.get>   /  this doesnt apply in the previous form
print(my_dict.get["captain"])

print("airplane model" in my_dict) # returns True
print("destination" in my_dict)