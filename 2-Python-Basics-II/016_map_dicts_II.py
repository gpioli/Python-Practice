# When applying the map function, we shouldn't be changing the original list
# so in order to solve this we can generate a copy of the original file

# The explanation for this is that when working with a dictionary, as it is not a primitive data type the object itself
# is not located in the heap memory. A reference to a dictionary is saved on the heap but the object itself is located
# on the stack memory

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


def add_taxes_v2(item):
    temporary_item = items.copy()
    temporary_item["taxes"] = temporary_item["price"] * 0.22
    return temporary_item


new_items = list(map(add_taxes_v2, items))
print(items)
print(new_items)

