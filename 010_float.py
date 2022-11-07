
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

print(x == y) # This returns False... so, how do we compare floats?

# format allows us to re format the number avoiding all the decimal precision
y_str = format(y, ".2g")
print('str => ', y_str)
print(y_str == str(x)) # This is one way
# But this is not a mathematical way...

print('*' * 10)

print(y,x)
tolerance = 0.00001
print(abs(x - y) < tolerance)

