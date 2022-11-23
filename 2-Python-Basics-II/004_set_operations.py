set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union (a + b without repetition)
set_c = set_a.union(set_b)
print(set_c)
# this does the same, but instead of using a method we use an operator
print(set_a | set_b)

# Intersections (elements in the intersection, or in both sets)
set_h = set_a.intersection(set_b)
print(set_h)
print(set_a & set_b)

# Difference (elements of the first set without the elements of the second set)
set_i = set_a.difference(set_b)
print(set_i)
print(set_a - set_b)

# Symmetric_difference -> its a union without common elements (intersection)
set_k = set_a.symmetric_difference(set_b)
print(set_k)
print(set_a ^ set_b)
