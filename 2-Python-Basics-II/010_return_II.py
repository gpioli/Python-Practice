# assigning more than one argument to a functions

def find_volume(length, width, depth):
    return length * width * depth


result = find_volume(10, 5, 4)
print(result)


# If we ran the function without one of the arguments, python will crash.
# We can fix this setting default values
def find_volume_II(length=1, width=1, depth=1):
    return length * width * depth


result_II = find_volume_II(2, 4)
print(result_II)


# We can also return more than one value per function
def falopa_function(string):
    return string, string * 2, 8


x = falopa_function("hello")  # returns a tuple
print(x)
