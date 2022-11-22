# and
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 < 10) # prints True
print(10 > 5 > 10) # prints False

#stock = int(input("Please input the stock available: "))
#print(stock >= 100 and stock <= 1000) #business logic


# or
print('or')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)


role = input('Insert permissions (admin or seller available): ')
print(role == 'admin' or role == 'seller')
