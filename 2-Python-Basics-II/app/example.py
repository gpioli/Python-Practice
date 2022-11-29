import main

# Here we will work with the duality of the modules (all .py files):
# This means that modules can be run as scripts directly from the terminal, or be executed from other files as
# imports...


# Let's begin:
# If we run the following line (14) as it is, this will also run the full main.py file
# So how do we solve this?
# Modularizing: we can put all the functionality inside a function in main.py, so it only runs explicitly
# (check main.py, from line 21) | (This wasn't a function, but now it is)

# print(main.data)

# But this comes with a problem: if we run directly the main.py it will not run (it looses its ability to be run as a
# script)
#
# Solution: generating an entry point in the main file:
# if __name__ == "__main__":
#     run()

print(main.data)
