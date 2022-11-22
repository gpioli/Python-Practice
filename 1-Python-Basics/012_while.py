### Working with While loop

# While

# This will execute infinitely
#while True:
#    print("This should print infinitely, but we cant stop it with ctrl + c or ctrl + F2 (PyCharm)" )


# Another while cicle:
print("First loop")
counter = 0

while counter < 10:
    counter += 1
    print(counter)


# Breaking the loop:
counter2 = 0
print("Second loop")
while counter2 < 20:
    counter2 += 1
    if counter2 == 15:
        break ### Here we breaf the flux
    print(counter2)

# Skipping one or more cycles:
counter3 = 0
print("Third loop")
while counter3 < 20:
    counter3 += 1
    if counter3 < 15: ### here we skip all the cycles where the counter is less than 15
        continue
    print(counter3)
