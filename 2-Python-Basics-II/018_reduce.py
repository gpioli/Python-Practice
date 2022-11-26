# Reduce
# Allows us to pick something and obtain ONE conclusion of that

import functools

numbers = [1, 2, 3, 4]
# This will do the running total
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)
