# Working with maps in dicts
from copy import copy

items = [
    {
        "product": "shirt",
        "price": 100
    },
    {
        "product": "trousers",
        "price": 200
    },
    {
        "product": "belt",
        "price": 50
    }
]

# What if I only want a list of the prices?

prices = list(map(lambda item: item["price"], items))
print(prices)


# Now we want to calculate the tax of the products
# Here we cannot use a lambda because we have more complexity, so we define a function
def add_taxes(item):
    item["taxes"] = item["price"] * 0.22
    return item


new_items = list(map(add_taxes, items))
print(items)
print(new_items)

# We must be careful with this modifications
# map is a function that is considered to not modify the data
# this is what happens in the first example, but not in the second example (there was a change in the original array

# A way to solve this... see next file (016_map_dicts):
