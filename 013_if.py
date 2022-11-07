# if

if True:
    print('This should execute')

if False:
    print('This should never execute')

'''
pet = input("That's your fav pet? ")

if pet == 'dog':
    print("wow wow!")

if pet == 'cat':
    print('miauuu!')
'''

# if else
stock = int(input('Please enter available stock: '))

if stock >= 100 and stock <= 1000:
    print("Stock is right")
else:
    print("Wrong stock input")

# elif

pet = input("That's your fav pet? ")

if pet == 'dog':
    print("wow wow!")

elif pet == 'cat':
    print('miauuu!')

elif pet == "fish":
    print("glu glu")

else:
    print("You're sooo boring!")