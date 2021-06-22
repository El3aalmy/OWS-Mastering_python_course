# ------------------------------------------
# -- Modules => Install external packages --
# ------------------------------------------
# [1] Module vs package  => package is a pack of modules 
# [2] External packages downloaded from the internet 
# [3] You can install packages with python package manager PIP
# [4] PIP install the package and its dependencies
# [5] Modules list ( https://docs.python.org/3/py-modindex.html )
# [6] Packages and modules directory ( https://pypi.org )
# [7] PIP manual ( https://pip.pypa.io/en/stable/reference/pip_install/ )
# -------------------------------------------------------------------

# pip --version             # Show virsion of pip 
# pip list                  # Show list of packages installed
# pip install ..            # Install package
# pip install .. ..         # Install mulitpule packages or modules
# pip install ..==version   # Install specific version of package
# pip install ..>=version   # Install version of newest version of it
# pip install pip --upgrade # If error => pip install --user pip --upgrade


import termcolor
import pyfiglet

# print(dir(pyfiglet))
print(pyfiglet.figlet_format("Hasan"))
print(termcolor.colored("Hasan", color="yellow"))

# print(help(termcolor))  # Show avaliable colors

print(termcolor.colored(pyfiglet.figlet_format("Hasan"), color="yellow"))
