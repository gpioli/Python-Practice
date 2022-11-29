# Working with iterables

# We have already worked with iterables:
for i in range(1, 11):
    print(i)

# But what is range?
my_iter = range(1, 11)
print(my_iter)
# Here it is not yet an iterable type
# When we use it inside a for, python automatically turns it into an iterator...

# But if we want, we can create manually an iterable
my_iter = iter(range(1, 3))
print(my_iter)
# And we can manage the way this is executed
print(next(my_iter))
print(next(my_iter))  # This is what a for does internally...
# This is useful as this consumes less memory compared to a range... which has to generate all the numbers in the range
# vector

# This will be useful specially for opening files (next classes)
# But if we exceed the number of iterations we will have a StopIteration error:
# print(next(my_iter))

