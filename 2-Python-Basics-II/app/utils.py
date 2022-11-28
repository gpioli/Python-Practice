# We create our first module, which is basically any .py file, that contains vars, functions, etc

def get_population():
    keys = ["col", "bol"]
    values = [300, 400]
    return keys, values


a = "Hello!"


def population_by_country(data, country):
    result = list(filter(lambda item: item["Country"] == country, data))
    return result


