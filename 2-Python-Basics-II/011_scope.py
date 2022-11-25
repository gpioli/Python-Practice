# https://www.w3schools.com/python/python_scope.asp

price = 100

print(price)  # this var has a GLOBAL scope, which means that can be accessed from anywhere between the py file


def increment():
    price = 200  # local context or scope is reachable only from inside the function
    price = price + 10
    print(price)
    x = 50


increment()

# This will break because variables declared inside functions are only reachable inside of them
# print(x)

