# -------------------------------------
# --- Modules => Create your module ---
# -------------------------------------

import sys
sys.path.append(r"C:\users")    # Add a new path of searching path of modules
print(sys.path)   # Show paths where python search for modules on it


import hasan 
# print(dir(hasan))     # Show functions in module

hasan.my_name_is("Hasan")
hasan.my_name_is("Ahmed")


# Alias 

import hasan as ee    # => ee is a alias name for module if module name inconsistent with other names 
# print(dir(hasan))

ee.my_name_is("Hasan")
ee.my_name_is("Ahmed")


# Alias name for function 

from hasan import my_name_is 

my_name_is("Ahmed")

from hasan import my_name_is as ss      # => ss is a alias name for function if function name inconsistent with other names 

ss("Hasan")
