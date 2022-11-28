# We are going to import the module created

import utils

keys, values = utils.get_population()
print(keys, values)

print(utils.a)

data = [
    {
        "Country": "Colombia",
        "Population": 500
    },
    {
        "Country": "Bolivia",
        "Population": 300
    }
]

result = utils.population_by_country(data, "Colombia")
print(result)

country = input("Please, type country name => ")
result_input = utils.population_by_country(data, country)
print(result_input)
