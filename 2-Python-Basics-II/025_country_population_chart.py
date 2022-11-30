import csv
import re


def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")  # We create a reader for our file
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


# This is a valid solution
def get_population(country_dict):
    population_dict = {
        "2022": country_dict["2022 Population"],
        "2020": country_dict["2020 Population"],
        "2015": country_dict["2015 Population"],
        "2010": country_dict["2010 Population"],
        "2000": country_dict["2000 Population"],
        "1990": country_dict["1990 Population"],
        "1980": country_dict["1980 Population"],
        "1970": country_dict["1970 Population"]
    }
    labels = population_dict.keys()
    values = population_dict.values()

    return labels, values


global_data = read_csv("./app/world_population.csv")
# print(global_data)
argentina_data = list(filter(lambda country: country["Country/Territory"] == "Argentina", global_data))
print(argentina_data)



argentina_population = list(filter(lambda item: item.keys(), argentina_data))
print(argentina_population)

for item in argentina_data:
    if item.keys().__contains__("Population"):
        print(item.keys())