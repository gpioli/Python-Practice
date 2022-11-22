name = "Nicolas"
print(type(name)) ##str

### Changing data type dinamically
name = 12
print(type(name))

# Again:
name = True
print(type(name))

# python inferes the data type (str)
print("Nicolas" + "Cage")
print(10 + 20)

# This would break (we cannot concatenate strings + bool
# print("Nicolas" + 12) # Cannot concatenate str and int

age = 12
#This will break
# print("Age: " + age)

# We need to transform the data type of the age:
print("Age: " + str(age)) # this conversion is explicit
print(f"Age: {age}") # Here the conversion is implicit (python inferes that has to
# work with str...

age = input("Please enter your age: ")
print(type(age))
age = int(age)
print(f"Your age in 10 years will be: {age + 10}")

