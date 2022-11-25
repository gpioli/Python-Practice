# https://www.w3schools.com/python/python_lambda.asp

# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression


# traditional function
def increment(x):
    return x + 1


result = increment(10)
print(result)


# converting it to a lambda function
# arguments: x
# output: x + 1

increment_v2 = lambda x : x + 1

result = increment_v2(20)
print(result)

# another lambda function
full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
text = full_name('gaston', 'pioli')
print(text)
