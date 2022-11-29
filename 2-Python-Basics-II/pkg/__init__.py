print("Package pkg initialized")

URL = "google.com"

# This line allows us to set all the imports that are done when importing from other module the package "pkg"
# (see line 28 of the file 2-Python-Basics-II/main.py)
from .mod_1 import fun_1, fun_2
from .mod_2 import fun_3, fun_4
