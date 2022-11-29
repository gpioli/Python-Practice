# We are learning how to import from packages (which are simply folders with modules)
# From python version 3.3 it isn't necessary to work with an __init__.py file, but if we work with previous versions,
# we will have to add the file

# From version 3.3, the file can be used to initialize a package (go to __init__,py to see how it works)

# from pkg.mod_1 import fun_1, fun_2
# from pkg.mod_2 import fun_3, fun_4

print(fun_1())
print(fun_2())

print(fun_3())
print(fun_4())

# notice the package is initialized only once, despite importing both packages
import pkg
print(pkg.URL)

# Despite this will work, notice that if we comment the imports, this will fail
print(pkg.mod_1.fun_1())
# Module not imported

# But we can automatize this by adding these lines to the init.py:
# import pkg.mod_1, pkg.mod_2

# Now we can comment the first two imports, and either way run this:
import pkg
print(pkg.URL)
print(pkg.mod_1.fun_1)
# This works because of the lines 7 and 8 from __init__.py
