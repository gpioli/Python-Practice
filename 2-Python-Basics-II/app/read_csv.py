import csv
import json

# This allows us to read the file as a list
# def read_csv(path):
#    with open(path, "r") as csvfile:
#        reader = csv.reader(csvfile, delimiter=",")  # We create a reader for our file
#        for row in reader:
#            print("***" * 5)
#            print(row)

# But what if we want to read this as a dictionary?
# Let's read the first row in order to get the headers:


# def read_csv(path):
#    with open(path, "r") as csvfile:
#         reader = csv.reader(csvfile, delimiter=",")  # We create a reader for our file
#         header = next(reader)
#         print(header)

# ['Rank', 'CCA3', 'Country/Territory', 'Capital', 'Continent', '2022 Population', '2020 Population', '2015 Population',
# '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population', 'Area (km²)',
# 'Density (per km²)', 'Growth Rate', 'World Population Percentage']


# Let's use a zip to join the header with the row:

# def read_csv(path):
#     with open(path, "r") as csvfile:
#         reader = csv.reader(csvfile, delimiter=",")  # We create a reader for our file
#         header = next(reader)
#         for row in reader:
#             iterable = zip(header, row)
#             print(list(iterable))


# Let's generate a dict from that iterable, using dictionary comprehension

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

if __name__ == "__main__":
    data = read_csv("./world_population.csv")
    print(data[0])

    # Extra: saving data to a json file
    # Serializing json
    # json_object = json.dumps(data, indent=4)
    # print(json_object)

