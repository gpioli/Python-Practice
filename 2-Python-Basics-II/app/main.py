# We are going to import the module created (utils)

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


def run():
    result = utils.population_by_country(data, "Colombia")
    print(result)

    country = input("Please, type country name => ")
    result_input = utils.population_by_country(data, country)
    print(result_input)


if __name__ == "__main__":
    run()
