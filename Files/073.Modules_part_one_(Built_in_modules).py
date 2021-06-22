# ------------------------------------
# --- Moduless => built in modules ---
# ------------------------------------
# [1] Modules is a file contain a set of functions 
# [2] You can import module in your app to help you
# [3] You can import multiple modules
# [4] You can create your own modules 
# [5] Modules saves your time 
# ---------------------------------------------------

# Import main module 

import random 
print(random)
print(f"Print random float number {random.random()}")


# Show all functions inside module 

import random 
print(dir(random))


# Import one or two funcitons from module 
# from module-name import function-name
from random import randint, random
print(f"Print random float {random()}")
print(f"Print random integer {randint(100, 900)}")
# print(f"Print random integer {random.randint(100, 900)}")
# This is a error => You import just a function not all module ( random not defined )

# from random import *      => Import all functions 
