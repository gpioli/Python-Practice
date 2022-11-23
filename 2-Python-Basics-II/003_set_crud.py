# Strings
print('')
set_countries = {'Colombia', 'Mexico', 'Bolivia'}
print(set_countries)

# lenght of a set
print(len(set_countries)) # 3

# Knowing if smth is IN a set
print('Colombia' in set_countries) # True
print('Peru' in set_countries) # False

# add elements
set_countries.add('Peru')
print(set_countries)
set_countries.add('Peru') # this wont repeat the operation - elements cant be added twice
print(set_countries)

# update
# similar to add, but can add several elements
set_countries.update({'Arg', 'Ecuador', 'Peru'})
print(set_countries)

# remove

set_countries.remove('Arg')
print(set_countries)

# If we try to remove an element that isnt inside a set, the program will break
#set_countries.remove("Venezuela")
# Instead, we can use discard | this wont break
set_countries.discard('Venezuela')

set_countries.add('Argentina')
print(set_countries)

# Cleaning the whole set
print('')
set_countries.clear()
print(set_countries)