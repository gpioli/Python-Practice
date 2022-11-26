# https://www.geeksforgeeks.org/higher-order-functions-in-python/
# A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an
# output


def increment(x):
    return x + 1


def high_ord_func(x, func):
    return x + func(x)


result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)


# defining higher order functions with lambdas
increment_v2 = lambda x: x + 1
high_ord_func_v2 = lambda x, func: x + func(x)
result_2 = high_ord_func_v2(2, increment_v2)
print(result_2)