# Handling errors allows us to keep executing our program despite the fact that something may not be going as intended
# initially...

# https://www.w3schools.com/python/python_try_except.asp

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

# Notice programs continues running and prints hello despite the error
print("Hello")

# Assert has its own exception handling embedded:
try:
    assert 1 != 1, "One is not equal to one"
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception("Under age not allowed")
except Exception as error:
    print(error)

print("Hello")

# We can join everything in a unique try block:

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

# Notice programs continues running and prints hello despite the error
print("Hello")

# Assert has its own exception handling embedded:
try:
    print(0/0)
    assert 1 != 1, "One is not equal to one"
    age = 10
    if age < 18:
        raise Exception("Under age not allowed")
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print("Hello 2")


# try:
#     pass
# except Exception as e:
#     raise
# else:
#     pass
# finally:
#     pass

# else executes when all the try block executes correctly (without exceptions)
# finally executes regardless exceptions happen or not
