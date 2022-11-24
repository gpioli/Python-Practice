import random

dict = {}

# adding values the old way...
for i in range(1,11):
    dict[i] = i*2

print(dict)

# With dictionaries comprehension

dict_v2 = { i: i * 2 for i in range(1, 11)}
print(dict_v2)

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100) * 1000000
print(population)

population_v2 = {country: random.randint(1, 100)*1000000 for country in countries}
print(population_v2)


# Final example
names = ['Lula', 'Lili', 'Leia']
ages = [12, 56, 98]

# zip function joins lists...
print(list(zip(names, ages)))
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

names2 = ['Lucia', 'Agustina', 'Gaston']
ages2 = [30, 22, 32]
contacts = {name: age for (name, age) in zip(names2, ages2)}

print(contacts)
