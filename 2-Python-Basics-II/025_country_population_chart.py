import csv
from app import read_csv, charts


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
    # In order to be able to make the charts, we need an array of the labels and an array of the values:
    #labels = population_dict.keys()
    #values = population_dict.values()

    return population_dict # labels, values


def get_population_for_chart(country_dict):
    population_dict = {
        # By default, when reading a csv values come as string, so we must cast them to int
        "2022": int(country_dict["2022 Population"]),
        "2020": int(country_dict["2020 Population"]),
        "2015": int(country_dict["2015 Population"]),
        "2010": int(country_dict["2010 Population"]),
        "2000": int(country_dict["2000 Population"]),
        "1990": int(country_dict["1990 Population"]),
        "1980": int(country_dict["1980 Population"]),
        "1970": int(country_dict["1970 Population"])
    }
    # In order to be able to make the charts, we need an array of the labels and an array of the values:
    labels = population_dict.keys()
    values = population_dict.values()

    return labels, values


global_data = read_csv.read_csv("./app/world_population.csv")
# print(global_data)
argentina_data_list = list(filter(lambda country: country["Country/Territory"] == "Argentina", global_data))
print(argentina_data_list)
if len(argentina_data_list) > 0:
    argentina_data = argentina_data_list[0]
    print(argentina_data)
    argentina_population_data = get_population(argentina_data)
    print(argentina_population_data)

# In order to make the graph we are going to work with the auxiliar function, that returns labels and values
    argentina_population_data_labels, argentina_population_data_values = get_population_for_chart(argentina_data)
    print(argentina_population_data_labels, argentina_population_data_values)

# Now we can plot:
charts.generate_bar_chart(argentina_population_data_labels, argentina_population_data_values)
